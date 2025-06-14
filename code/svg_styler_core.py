# svg_styler_core.py

import xml.etree.ElementTree as ET
import re
import os
import uuid
import io
import argparse
import base64

# --- Dependency Check and Imports ---
try:
    import cairosvg
except ImportError:
    print("Dependency Error: CairoSVG is not installed. This is required for PNG output.")
    print("Please install with: pip install cairosvg")
    # We don't exit here, as SVG generation might still work, but PNG saving will fail.
    cairosvg = None

try:
    from country_data import COUNTRY_COLORS, COUNTRY_CODES
except ImportError:
    print("File Not Found: Could not import from country_data.py.")
    print("Please ensure it is in the same directory as this script.")
    exit()

SVG_NAMESPACE = "http://www.w3.org/2000/svg"
XLINK_NAMESPACE = "http://www.w3.org/1999/xlink"
ET.register_namespace('', SVG_NAMESPACE)
ET.register_namespace('xlink', XLINK_NAMESPACE)
CODE_TO_COUNTRY_NAME = {code: name for name, code in COUNTRY_CODES.items()}
COUNTRY_NAMES_SORTED = sorted(list(COUNTRY_CODES.keys()))

# --- SVG Processing Logic ---
def get_simple_path_bbox(d_attr):
    if not d_attr: return None
    points_x, points_y = [], []
    path_commands = re.findall(r"([mMlLhHvVcCsSqQtTaAzZ])([^mMlLhHvVcCsSqQtTaAzZ]*)", d_attr)
    current_x, current_y = 0, 0
    start_of_subpath_x, start_of_subpath_y = 0, 0
    for cmd_idx, (cmd, params_str) in enumerate(path_commands):
        params = [float(p) for p in re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", params_str)]
        idx = 0; is_relative = cmd.islower(); cmd_upper = cmd.upper(); original_cmd_upper = cmd_upper
        if cmd_upper == 'M':
            px = params[idx] + (current_x if is_relative and cmd_idx > 0 else 0)
            py = params[idx+1] + (current_y if is_relative and cmd_idx > 0 else 0)
            points_x.append(px); points_y.append(py); current_x, current_y = px, py
            start_of_subpath_x, start_of_subpath_y = px, py; idx += 2; cmd_upper = 'L'
        while idx < len(params):
            if cmd_upper == 'L':
                px = params[idx] + (current_x if is_relative else 0); py = params[idx+1] + (current_y if is_relative else 0)
                points_x.append(px); points_y.append(py); current_x, current_y = px, py; idx += 2
            elif cmd_upper == 'H':
                px = params[idx] + (current_x if is_relative else 0); py = current_y
                points_x.append(px); points_y.append(py); current_x = px; idx += 1
            elif cmd_upper == 'V':
                px = current_x; py = params[idx] + (current_y if is_relative else 0)
                points_x.append(px); points_y.append(py); current_y = py; idx += 1
            elif cmd_upper in ['C', 'S', 'Q', 'T', 'A']:
                num_params = {'C':6,'S':4,'Q':4,'T':2,'A':7}.get(cmd_upper,0)
                if not num_params or idx + num_params > len(params): break
                px = params[idx+num_params-2]+(current_x if is_relative else 0); py = params[idx+num_params-1]+(current_y if is_relative else 0)
                points_x.append(px); points_y.append(py); current_x,current_y=px,py; idx+=num_params
            else: break
        if original_cmd_upper == 'Z' and points_x: current_x, current_y = start_of_subpath_x, start_of_subpath_y
    if not points_x or not points_y: return {"x":0,"y":0,"width":1,"height":1}
    min_x,max_x=min(points_x),max(points_x); min_y,max_y=min(points_y),max(points_y)
    return {"x":min_x,"y":min_y,"width":max_x-min_x if max_x>min_x else 1,"height":max_y-min_y if max_y>min_y else 1}

def create_gradient_definition(defs_element, colors, gradient_id_base, gradient_direction, transition_width_percent=10):
    gradient_id = f"{gradient_id_base}-{gradient_direction}-gradient-{uuid.uuid4().hex[:6]}"
    coords = {"x1": "0%", "y1": "0%", "x2": ("0%" if gradient_direction == "vertical" else "100%"), "y2": ("100%" if gradient_direction == "vertical" else "0%")}
    gradient_element = ET.SubElement(defs_element, f"{{{SVG_NAMESPACE}}}linearGradient", {"id": gradient_id, **coords})
    num_colors = len(colors)
    if num_colors == 0: return None
    if num_colors == 1:
        ET.SubElement(gradient_element, f"{{{SVG_NAMESPACE}}}stop", {"offset": "0%", "style": f"stop-color:{colors[0]}"})
        return gradient_id
    softness = transition_width_percent / 100.0
    band_width = 100.0 / num_colors
    transition_size = band_width * softness
    for i, color in enumerate(colors):
        band_start = i * band_width
        band_end = (i + 1) * band_width
        plateau_start = band_start + (transition_size / 2.0)
        plateau_end = band_end - (transition_size / 2.0)
        if i == 0: plateau_start = 0
        if i == num_colors - 1: plateau_end = 100
        if plateau_start >= plateau_end:
            center_pos = band_start + (band_width / 2.0)
            ET.SubElement(gradient_element, f"{{{SVG_NAMESPACE}}}stop", {"offset": f"{center_pos:.2f}%", "style": f"stop-color:{color}"})
        else:
            ET.SubElement(gradient_element, f"{{{SVG_NAMESPACE}}}stop", {"offset": f"{plateau_start:.2f}%", "style": f"stop-color:{color}"})
            ET.SubElement(gradient_element, f"{{{SVG_NAMESPACE}}}stop", {"offset": f"{plateau_end:.2f}%", "style": f"stop-color:{color}"})
    return gradient_id

def modify_leaf_fill(root_element, defs_element, layer_group, leaf_id_method, leaf_params):
    country_code = leaf_params['country_code']
    country_name = CODE_TO_COUNTRY_NAME.get(country_code)
    if not country_name or country_name not in COUNTRY_COLORS:
        return False, f"Data not found for code: {country_code}"
    target_path_element = None
    all_paths_in_group = [el for el in list(layer_group) if el.tag == f"{{{SVG_NAMESPACE}}}path"]
    d_start = leaf_id_method['d_start']
    for path_el_candidate in all_paths_in_group:
        if 'processed' in path_el_candidate.attrib: continue
        if path_el_candidate.get("d", "").strip().startswith(d_start):
            target_path_element = path_el_candidate
            break
    if target_path_element is None: return False, f"Path not found for {leaf_params['leaf_name']}"
    target_path_element.set('processed', 'true')

    leaf_d_attribute = target_path_element.get("d")
    if not leaf_d_attribute: return False, "Target path has no 'd' attribute."
    
    unique_id_base = f"{country_code}-{leaf_params['leaf_name'].lower()}-{uuid.uuid4().hex[:4]}"
    fill_applied_successfully = False

    if leaf_params['fill_type'] == "flag-svg":
        flag_svg_path = os.path.join("flags", f"{country_code}.svg")
        if os.path.exists(flag_svg_path):
            try:
                # 1. Get flag's original dimensions
                flag_tree = ET.parse(flag_svg_path)
                flag_root = flag_tree.getroot()
                flag_viewbox = flag_root.get("viewBox", "0 0 100 100").split()
                flag_w = float(flag_root.get("width", flag_viewbox[2] if len(flag_viewbox) == 4 else "100"))
                flag_h = float(flag_root.get("height", flag_viewbox[3] if len(flag_viewbox) == 4 else "100"))
                flag_aspect_ratio = flag_w / flag_h if flag_h > 0 else 1

                # 2. Get leaf's bounding box
                bbox = get_simple_path_bbox(leaf_d_attribute)
                if bbox and bbox['width'] > 0 and bbox['height'] > 0:
                    # 3. Calculate "cover" dimensions for the image
                    bbox_w, bbox_h = bbox['width'], bbox['height']
                    bbox_aspect_ratio = bbox_w / bbox_h
                    
                    img_w, img_h = (bbox_w, bbox_w / flag_aspect_ratio) if bbox_aspect_ratio > flag_aspect_ratio else (bbox_h * flag_aspect_ratio, bbox_h)

                    # 4. Apply zoom
                    zoom_factor = leaf_params.get('zoom', 100.0) / 100.0
                    final_img_w = img_w * zoom_factor
                    final_img_h = img_h * zoom_factor
                    
                    # 5. Calculate centered position and apply pan
                    img_x = bbox['x'] + (bbox_w - final_img_w) / 2
                    img_y = bbox['y'] + (bbox_h - final_img_h) / 2
                    
                    overhang_x = max(0, final_img_w - bbox_w)
                    overhang_y = max(0, final_img_h - bbox_h)
                    img_x -= (leaf_params.get('pan_x', 0.0) / 100.0) * (overhang_x / 2.0)
                    img_y -= (leaf_params.get('pan_y', 0.0) / 100.0) * (overhang_y / 2.0)

                    # 6. Read and Base64-encode the flag SVG
                    with open(flag_svg_path, "rb") as f:
                        encoded_flag = base64.b64encode(f.read()).decode('ascii')
                    data_uri = f"data:image/svg+xml;base64,{encoded_flag}"

                    # 7. Create the <pattern> element
                    pattern_id = f"pattern-{unique_id_base}"
                    pattern_el = ET.SubElement(defs_element, f"{{{SVG_NAMESPACE}}}pattern", {
                        "id": pattern_id,
                        "patternUnits": "userSpaceOnUse",
                        "x": str(img_x),
                        "y": str(img_y),
                        "width": str(final_img_w),
                        "height": str(final_img_h)
                    })
                    
                    # 8. Create the <image> inside the pattern
                    ET.SubElement(pattern_el, f"{{{SVG_NAMESPACE}}}image", {
                        "x": "0",
                        "y": "0",
                        "width": str(final_img_w),
                        "height": str(final_img_h),
                        f"{{{XLINK_NAMESPACE}}}href": data_uri
                    })
                    
                    # 9. Apply the pattern fill to the target path
                    target_path_element.set("fill", f"url(#{pattern_id})")
                    if 'class' in target_path_element.attrib:
                        del target_path_element.attrib['class']

                    fill_applied_successfully = True
            except Exception as e:
                # Fallback to gradient on any error
                print(f"Warning: Failed to apply SVG flag pattern for {country_name}. Reason: {e}. Falling back to gradient.")
                pass

    if leaf_params['fill_type'] == "gradient" or not fill_applied_successfully:
        if target_path_element in list(layer_group):
            colors = COUNTRY_COLORS[country_name]
            gradient_id = create_gradient_definition(defs_element, colors, unique_id_base, leaf_params['direction'], leaf_params.get('transition', 10))
            if gradient_id:
                target_path_element.set("fill", f"url(#{gradient_id})")
                if 'class' in target_path_element.attrib: del target_path_element.attrib['class']
    
    return True, f"Processed {leaf_params['leaf_name']}."

def process_svg(top_params=None, right_params=None, left_params=None):
    """Generates the final SVG content as a string."""
    input_svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg id="Layer_2" data-name="Layer 2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 640 510">
  <defs>
    <style> .cls-1 { fill: #088180; } .cls-1, .cls-2 { stroke-width: 0px; } .cls-2 { fill: #fff; } </style>
  </defs>
  <g id="Layer_1-2" data-name="Layer 1">
    <path class="cls-1" d="m200.76,164.31s0,.02-.01.04c.01-.02.01-.03.01-.04Z"/><path class="cls-1" d="m336.98,299.22s-.03.01-.04.02c.02-.01.03-.01.04-.02Z"/><path class="cls-2" d="m335.97,494.14c2.17,4.26.47,9.47-3.78,11.64-4.27,2.17-9.48.47-11.64-3.79-2.17-4.27-.49-9.47,3.79-11.63,4.26-2.17,9.47-.47,11.63,3.78Z"/><path class="cls-2" d="m92.66,263.59c23.4,46.34,57.14,86.7,98.33,117.92,30.62-17.89,50.22-52.01,47.69-89.8-2.04-30.52-18.07-56.76-41.39-72.92-7.45-5.16-15.62-9.29-24.34-12.22-3.41-1.13-6.91-2.08-10.47-2.83-42.4-13.57-75.36-49.41-84.13-94.6l-.14-.1C27.48,144.39-4.01,204.67.41,270.87c3.66,54.84,31.24,102.41,71.85,133.18-.18-.14-.34-.28-.52-.42,14.29,11.07,33.1,16.81,52.58,15.51,23.41-1.57,43.64-13.48,56.61-30.95-38.23-34.09-68.6-76.67-88.27-124.61Zm-35.79,124.1s.01.02.03.03t-.03-.03Z"/><path class="cls-2" d="m284.59,97c-12.86,39.08-16.58,80.63-10.99,121.21,27.19,7.15,57.32-1,77.07-23.6,15.96-18.25,21.7-41.94,17.67-64.09-1.28-7.07-3.54-13.98-6.8-20.49-1.27-2.55-2.69-5.03-4.27-7.46-16.16-31.37-14.56-69.93,5.86-100.17v-.14c-48.26-8.63-99.72,7.51-134.33,47.09-28.7,32.81-39.9,74.91-34.39,114.94-.02-.18-.04-.35-.05-.52,1.8,14.22,9.12,27.98,20.78,38.16,14,12.25,32,16.92,49.07,14.38-2.3-40.53,4.54-81.42,20.38-119.31Zm-89.63,49.5s0,.02-.02.04c.02-.02.02-.03.02-.04Z"/><path class="cls-2" d="m465.83,320.23c-50.27,25.39-94.07,62.01-127.93,106.7,19.4,33.22,56.42,54.48,97.43,51.75,33.12-2.21,61.59-19.61,79.13-44.93,5.6-8.07,10.09-16.96,13.25-26.42,1.23-3.7,2.25-7.49,3.08-11.35,14.72-46,53.61-81.77,102.64-91.29l.12-.13c-38.36-55.05-103.77-89.23-175.59-84.43-59.53,3.97-111.13,33.87-144.53,77.94.15-.19.31-.36.46-.55-12.02,15.51-18.24,35.91-16.82,57.05,1.68,25.4,14.61,47.35,33.56,61.42,37-41.46,83.2-74.42,135.21-95.77Zm-134.66-38.82s-.02,0-.02.02c0-.02.01-.02.02-.02Z"/><path class="cls-2" d="m269.5,241.69c-.11.05-.23.11-.35.17-1.69,5.97-3.23,12.03-4.57,18.18-18.98,87.93,3.98,175.16,55.42,240.84,5.66-1.54,11.11-3.67,16.27-6.28-53.72-69.9-79.88-160.26-66.77-252.92Z"/><path class="cls-2" d="m192.17,390.42c-.03.13-.04.28-.06.41,4.35,4.94,8.88,9.79,13.59,14.52,30.01,29.98,64.64,52.48,101.6,67.51-4.39-6.59-8.54-13.37-12.42-20.29-36.69-14.44-71.5-35.14-102.72-62.16Z"/>
  </g>
</svg>"""
    try:
        # Clean up any previously generated elements before processing
        root = ET.fromstring(input_svg_content)
        for path in root.findall(f".//{{{SVG_NAMESPACE}}}path[@processed]"):
            del path.attrib['processed']
        
        defs_element = root.find(f".//{{{SVG_NAMESPACE}}}defs")
        if defs_element is None: defs_element = ET.SubElement(root, f"{{{SVG_NAMESPACE}}}defs")
        
        # Clear previous gradients and patterns
        for item in list(defs_element):
            item_id = item.get('id', '')
            if 'gradient' in item_id or 'pattern' in item_id:
                defs_element.remove(item)

    except ET.ParseError as e:
        return f"Fatal: Could not parse SVG template: {e}", None
        
    layer_group = root.find(f".//{{{SVG_NAMESPACE}}}g[@id='Layer_1-2']")
    if layer_group is None:
        return "Fatal: Main layer group 'Layer_1-2' not found.", None
        
    if left_params:
        left_leaf_id_method = {'type': 'specific_d', 'd_start': "m92.66,263.59c"}
        modify_leaf_fill(root, defs_element, layer_group, left_leaf_id_method, left_params)
    if top_params:
        top_leaf_id_method = {'type': 'specific_d', 'd_start': "m284.59,97c"}
        modify_leaf_fill(root, defs_element, layer_group, top_leaf_id_method, top_params)
    if right_params:
        right_leaf_id_method = {'type': 'specific_d', 'd_start': "m465.83,320.23c"}
        modify_leaf_fill(root, defs_element, layer_group, right_leaf_id_method, right_params)
        
    return "SVG content generated.", ET.tostring(root, encoding="unicode", method="xml")


# --- Centralized Argument Parser ---
def create_argument_parser(is_cli=False):
    """
    Creates and configures an ArgumentParser.
    :param is_cli: If True, adds CLI-specific arguments like --output.
    :return: An instance of argparse.ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        description="Styles an SVG logo with country flags or gradients.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # General options
    parser.add_argument(
        '--preset',
        type=str,
        help="Use a predefined preset from presets.json (e.g., 'it-en').\n"
             "These values can be overridden by other specific CLI flags."
    )

    if is_cli:
        parser.add_argument(
            '-o', '--output',
            required=True,
            help="For single generation: Output file path (without extension), e.g., 'my_logo'.\n"
                 "For --generate-all: Output directory path, e.g., 'output_logos'."
        )
        parser.add_argument(
            '--generate-all',
            action='store_true',
            help="Generate logos for all entries in presets.json.\n"
                 "The --output argument will be used as the destination directory."
        )
        parser.add_argument(
            '--png-width',
            type=int,
            default=600,
            help="Width of the output PNG file in pixels. Default is 600."
        )

    # --- Leaf Arguments Groups ---
    leaf_groups = {'left': 'Left', 'top': 'Top', 'right': 'Right'}
    for prefix, title in leaf_groups.items():
        group = parser.add_argument_group(f'{title} Leaf Options')
        group.add_argument(f'--{prefix}-country', type=str, help=f'Name of the country for the {prefix} leaf.')
        group.add_argument(f'--{prefix}-fill-type', choices=['gradient', 'flag-svg'], default='gradient', help=f'Fill type for the {prefix} leaf.')
        group.add_argument(f'--{prefix}-direction', choices=['horizontal', 'vertical'], default='horizontal', help='Direction for gradient fill.')
        group.add_argument(f'--{prefix}-transition', type=float, default=20.0, help='Transition softness for gradient (1-99).')
        group.add_argument(f'--{prefix}-zoom', type=float, default=100.0, help='Zoom level for flag fill (25-400).')
        group.add_argument(f'--{prefix}-pan-x', type=float, default=0.0, help='Horizontal pan for flag fill (-100 to 100).')
        group.add_argument(f'--{prefix}-pan-y', type=float, default=0.0, help='Vertical pan for flag fill (-100 to 100).')

    return parser


def generate_and_save_logo(output_path, top_params=None, right_params=None, left_params=None, png_width=1200):
    """Generates the SVG, saves it, and saves PNG and PDF versions."""
    print("Generating SVG content...")
    status, svg_content = process_svg(top_params=top_params, right_params=right_params, left_params=left_params)

    if not svg_content:
        print(f"Error: Could not generate SVG. Reason: {status}")
        return

    base_path, _ = os.path.splitext(output_path)
    svg_filepath = f"{base_path}.svg"
    png_filepath = f"{base_path}.png"
    pdf_filepath = f"{base_path}.pdf"

    try:
        os.makedirs(os.path.dirname(svg_filepath), exist_ok=True)
        with open(svg_filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"Successfully saved: {svg_filepath}")

        if cairosvg:
            print(f"Generating PNG (width: {png_width}px)...")
            cairosvg.svg2png(bytestring=svg_content.encode('utf-8'), write_to=png_filepath, output_width=png_width)
            print(f"Successfully saved: {png_filepath}")

            print("Generating PDF...")
            cairosvg.svg2pdf(bytestring=svg_content.encode('utf-8'), write_to=pdf_filepath)
            print(f"Successfully saved: {pdf_filepath}")
        else:
            print("Skipping PNG and PDF generation: CairoSVG not found.")

    except Exception as e:
        print(f"An error occurred while saving files: {e}")