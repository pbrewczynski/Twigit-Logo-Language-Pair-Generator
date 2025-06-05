#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import re
import os
import argparse
import uuid

# --- Imports and Setup (Keep as before) ---
try:
    import cairosvg
except ImportError:
    print("DEBUG: CairoSVG import failed or not found.") 
    cairosvg = None
else:
    print("DEBUG: CairoSVG imported successfully.")

try:
    from country_data import COUNTRY_COLORS, COUNTRY_CODES 
except ImportError:
    print("Error: Could not import from country_data.py.")
    exit(1)

SVG_NAMESPACE = "http://www.w3.org/2000/svg"
XLINK_NAMESPACE = "http://www.w3.org/1999/xlink"
ET.register_namespace('', SVG_NAMESPACE)
ET.register_namespace('xlink', XLINK_NAMESPACE)
CODE_TO_COUNTRY_NAME = {code: name for name, code in COUNTRY_CODES.items()}

# --- Helper Functions (get_initial_y_from_d, create_gradient_definition, create_flag_pattern_definition, get_simple_path_bbox - keep as in last correct version) ---
def get_initial_y_from_d(d_attr):
    if not d_attr: return None
    match = re.match(r"^\s*[mM]\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s*[, ]\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)", d_attr.strip())
    return float(match.group(2)) if match else None

def create_gradient_definition(defs_element, colors, gradient_id_base, gradient_direction):
    gradient_id = f"{gradient_id_base}-{gradient_direction}-gradient-{uuid.uuid4().hex[:6]}"
    existing_gradient = defs_element.find(f".//{{{SVG_NAMESPACE}}}linearGradient[@id='{gradient_id}']")
    if existing_gradient is not None: defs_element.remove(existing_gradient)
    coords = {"x1": "0%", "y1": "0%", "x2": ("0%" if gradient_direction == "vertical" else "100%"), "y2": ("100%" if gradient_direction == "vertical" else "0%")}
    gradient_element = ET.SubElement(defs_element, f"{{{SVG_NAMESPACE}}}linearGradient", {"id": gradient_id, **coords})
    num_colors = len(colors)
    if num_colors == 1:
        ET.SubElement(gradient_element, f"{{{SVG_NAMESPACE}}}stop", {"offset": "0%", "style": f"stop-color:{colors[0]};stop-opacity:1"})
        ET.SubElement(gradient_element, f"{{{SVG_NAMESPACE}}}stop", {"offset": "100%", "style": f"stop-color:{colors[0]};stop-opacity:1"})
    else:
        for i, color in enumerate(colors):
            offset = (i / (num_colors - 1)) * 100
            ET.SubElement(gradient_element, f"{{{SVG_NAMESPACE}}}stop", {"offset": f"{offset:.2f}%", "style": f"stop-color:{color};stop-opacity:1"})
    return gradient_id

def create_flag_pattern_definition(defs_element, country_code, pattern_id_base):
    pattern_id = f"{pattern_id_base}-flag-pattern-{uuid.uuid4().hex[:6]}"
    flag_svg_path = os.path.join("flags", f"{country_code}.svg")
    if not os.path.exists(flag_svg_path):
        print(f"Warning: Flag SVG for {country_code} not found at '{flag_svg_path}'.")
        return None
    try:
        flag_tree = ET.parse(flag_svg_path)
        flag_root = flag_tree.getroot()
    except Exception as e:
        print(f"Warning: Could not load/parse flag SVG '{flag_svg_path}': {e}.")
        return None
    existing_pattern = defs_element.find(f".//{{{SVG_NAMESPACE}}}pattern[@id='{pattern_id}']")
    if existing_pattern is not None: defs_element.remove(existing_pattern)
    flag_viewbox = flag_root.get("viewBox", "0 0 100 100")
    vb_parts = flag_viewbox.split()
    p_width = flag_root.get("width", vb_parts[2] if len(vb_parts) == 4 else "100")
    p_height = flag_root.get("height", vb_parts[3] if len(vb_parts) == 4 else "100")
    pattern_attribs = {"id": pattern_id, "patternUnits": "userSpaceOnUse", "width": p_width, "height": p_height, "viewBox": flag_viewbox, "preserveAspectRatio": "xMidYMid slice"}
    pattern_element = ET.SubElement(defs_element, f"{{{SVG_NAMESPACE}}}pattern", pattern_attribs)
    skip_tags = ["defs", "style", "metadata", "title", "desc", "sodipodi:namedview", "inkscape:perspective"]
    for child in flag_root:
        tag_name = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        if tag_name not in skip_tags:
            pattern_element.append(child)
    return pattern_id

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
            px = params[idx] + (current_x if is_relative and cmd_idx > 0 and (points_x or points_y) else 0) 
            py = params[idx+1] + (current_y if is_relative and cmd_idx > 0 and (points_x or points_y) else 0)
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
                if cmd_upper=='C': points_x.extend([params[idx]+(current_x if is_relative else 0), params[idx+2]+(current_x if is_relative else 0)]); points_y.extend([params[idx+1]+(current_y if is_relative else 0), params[idx+3]+(current_y if is_relative else 0)])
                elif cmd_upper in ['S','Q']: points_x.append(params[idx]+(current_x if is_relative else 0)); points_y.append(params[idx+1]+(current_y if is_relative else 0))
                px = params[idx+num_params-2]+(current_x if is_relative else 0); py = params[idx+num_params-1]+(current_y if is_relative else 0)
                points_x.append(px); points_y.append(py); current_x,current_y=px,py; idx+=num_params
            else: break
        if original_cmd_upper == 'Z' and points_x: current_x, current_y = start_of_subpath_x, start_of_subpath_y
    if not points_x or not points_y: return {"x":0,"y":0,"width":1,"height":1}
    min_x,max_x=min(points_x),max(points_x); min_y,max_y=min(points_y),max(points_y)
    return {"x":min_x,"y":min_y,"width":max_x-min_x if max_x>min_x else 1,"height":max_y-min_y if max_y>min_y else 1}

# --- New Core Logic Function ---
def modify_leaf_fill(root_element, defs_element, layer_group, leaf_id_method, leaf_params):
    """
    Identifies a leaf based on `leaf_id_method` and applies fill based on `leaf_params`.
    `leaf_id_method` is a dictionary like:
        {'type': 'specific_d', 'd_start': 'm284.59,97c...'} or
        {'type': 'y_coord', 'class_filter': 'cls-2'/'any', 'select': 'min_y'/'max_x_center'}
    `leaf_params` is a dictionary like:
        {'country_code': 'fr', 'fill_type': 'gradient', 'direction': 'horizontal', 'leaf_name': 'Top'}
    Returns True if modification was attempted (successful or fallback), False if leaf not found.
    """
    country_code = leaf_params['country_code']
    fill_type = leaf_params['fill_type']
    gradient_direction = leaf_params['direction']
    leaf_name = leaf_params['leaf_name'] # For logging

    country_name = CODE_TO_COUNTRY_NAME.get(country_code)
    if not country_name:
        print(f"Warning ({leaf_name} Leaf): Country code '{country_code}' not recognized. Skipping this leaf.")
        return False
    if country_name not in COUNTRY_COLORS:
         print(f"Warning ({leaf_name} Leaf): Colors for '{country_name}' not defined. Skipping this leaf.")
         return False


    target_path_element = None
    target_path_index = -1
    identified_by_str = "None"

    all_paths_in_group = [el for el in list(layer_group) if el.tag == f"{{{SVG_NAMESPACE}}}path"]

    if leaf_id_method['type'] == 'specific_d':
        d_start = leaf_id_method['d_start']
        for path_el_candidate in all_paths_in_group:
            if path_el_candidate.get("d", "").strip().startswith(d_start):
                target_path_element = path_el_candidate
                identified_by_str = f"specific d-attribute '{d_start[:20]}...'"
                break
    elif leaf_id_method['type'] == 'geometric':
        # This needs more sophisticated geometric selection, e.g., "most to the right"
        # For now, we'll use a placeholder or you can refine this
        # Example: find path with largest starting X among cls-2
        # This is a placeholder, as "right leaf" might need more complex logic than "top leaf"
        max_x = -float('inf')
        paths_to_check = all_paths_in_group
        if leaf_id_method.get('class_filter') == 'cls-2':
            paths_to_check = [p for p in all_paths_in_group if p.get("class") == "cls-2"]
        
        if not paths_to_check and leaf_id_method.get('class_filter') == 'cls-2': # Fallback if no cls-2
            paths_to_check = all_paths_in_group
            print(f"DEBUG ({leaf_name} Leaf): No cls-2 paths, checking all paths for geometric ID.")


        for path_el_candidate in paths_to_check:
            # Avoid re-selecting the top leaf if it was already processed
            if 'processed_paths' in leaf_id_method and path_el_candidate in leaf_id_method['processed_paths']:
                continue

            d_attr = path_el_candidate.get("d", "")
            # Simplified: using initial X of the path for "right-most" among candidates
            match_first_x = re.match(r"^\s*[mM]\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s*[, ]", d_attr.strip())
            if match_first_x:
                current_x = float(match_first_x.group(1))
                if current_x > max_x:
                    max_x = current_x
                    target_path_element = path_el_candidate
                    identified_by_str = f"geometric (max_x={max_x:.2f}, class: {path_el_candidate.get('class', 'N/A')})"
    else: # Default to top-leaf y_coord logic if type is unclear
        min_y = float('inf')
        paths_to_check = all_paths_in_group
        class_filter = leaf_id_method.get('class_filter', 'cls-2') # Default to cls-2
        if class_filter == 'cls-2':
            cls2_paths = [p for p in all_paths_in_group if p.get("class") == "cls-2"]
            paths_to_check = cls2_paths if cls2_paths else all_paths_in_group # Fallback if no cls-2
        
        for path_el_candidate in paths_to_check:
            if 'processed_paths' in leaf_id_method and path_el_candidate in leaf_id_method['processed_paths']:
                continue
            y_coord = get_initial_y_from_d(path_el_candidate.get("d",""))
            if y_coord is not None and y_coord < min_y:
                min_y = y_coord
                target_path_element = path_el_candidate
                identified_by_str = f"min Y ({min_y:.2f}, class: {path_el_candidate.get('class', 'N/A')})"


    if target_path_element is None:
        print(f"Error ({leaf_name} Leaf): Could not identify target path. Method: {leaf_id_method}, Last identified_by: {identified_by_str}")
        return False
    
    try:
        target_path_index = list(layer_group).index(target_path_element)
    except ValueError:
        print(f"ERROR ({leaf_name} Leaf): Identified path not in layer_group's direct children. This should not happen.")
        return False # Cannot proceed with replacement

    print(f"DEBUG ({leaf_name} Leaf): Successfully identified. Element: {target_path_element}, Method: {identified_by_str}, Index: {target_path_index}")
    leaf_d_attribute = target_path_element.get("d")
    if not leaf_d_attribute: 
        print(f"Error ({leaf_name} Leaf): Target path has no 'd' attribute.")
        return False

    # Mark this path as processed to avoid re-selecting for other leaves
    if 'processed_paths' in leaf_id_method:
        leaf_id_method['processed_paths'].append(target_path_element)


    # --- Apply Fill ---
    pattern_id_base = f"{country_code}-{leaf_name.lower().replace(' ','')}-{uuid.uuid4().hex[:4]}"
    fill_applied_successfully = False

    if fill_type == "flag-svg":
        print(f"Info ({leaf_name} Leaf): Attempting flag SVG clip-path for {country_name}.")
        pattern_id = create_flag_pattern_definition(defs_element, country_code, pattern_id_base)
        if pattern_id:
            clip_path_id = f"clip-{pattern_id_base}" # Simpler clip_path ID
            clip_path_el = ET.SubElement(defs_element, f"{{{SVG_NAMESPACE}}}clipPath", {"id": clip_path_id})
            ET.SubElement(clip_path_el, f"{{{SVG_NAMESPACE}}}path", {"d": leaf_d_attribute})
            bbox = get_simple_path_bbox(leaf_d_attribute)
            bbox_attrs = {"x":str(bbox['x']),"y":str(bbox['y']),"width":str(bbox['width']),"height":str(bbox['height'])} if bbox else {"width":"150%","height":"150%","x":"-25%","y":"-25%"}
            clipped_group = ET.Element(f"{{{SVG_NAMESPACE}}}g", {"clip-path": f"url(#{clip_path_id})"})
            ET.SubElement(clipped_group, f"{{{SVG_NAMESPACE}}}rect", {**bbox_attrs, "fill": f"url(#{pattern_id})"})
            
            if target_path_index != -1 and target_path_index < len(list(layer_group)) and list(layer_group)[target_path_index] is target_path_element:
                layer_group.remove(target_path_element)
                layer_group.insert(target_path_index, clipped_group)
                print(f"Info ({leaf_name} Leaf): Applied flag SVG pattern for {country_name}.")
                fill_applied_successfully = True
            else:
                print(f"ERROR ({leaf_name} Leaf): Mismatch/invalid index for replacement. Flag SVG fill failed.")
                fill_applied_successfully = False
        else:
            print(f"Warning ({leaf_name} Leaf): Flag SVG pattern creation failed. Falling back to gradient.")
            fill_applied_successfully = False

    if fill_type == "gradient" or (fill_type == "flag-svg" and not fill_applied_successfully):
        if target_path_element in list(layer_group): # Check if original path is still there for gradient
            colors = COUNTRY_COLORS[country_name]
            gradient_id = create_gradient_definition(defs_element, colors, pattern_id_base, gradient_direction)
            target_path_element.set("fill", f"url(#{gradient_id})")
            if 'class' in target_path_element.attrib: target_path_element.attrib.pop('class')
            print(f"Info ({leaf_name} Leaf): Applied {gradient_direction} gradient for {country_name}.")
        elif not (fill_type == "flag-svg" and fill_applied_successfully):
            print(f"ERROR ({leaf_name} Leaf): Target path for gradient unavailable.")
    
    return True # Modification was attempted


# --- Main execution ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Apply fills to specific leaves in an SVG.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    # Top Leaf Arguments
    parser.add_argument("--top-country", metavar="CC", choices=CODE_TO_COUNTRY_NAME.keys(), help="2-letter country code for the top leaf.")
    parser.add_argument("--top-fill-type", choices=["gradient", "flag-svg"], default="gradient", help="Fill type for top leaf. Default: gradient.")
    parser.add_argument("--top-direction", choices=["horizontal", "vertical"], default="horizontal", help="Gradient direction for top leaf. Default: horizontal.")

    # Right Leaf Arguments
    parser.add_argument("--right-country", metavar="CC", choices=CODE_TO_COUNTRY_NAME.keys(), help="2-letter country code for the right leaf.")
    parser.add_argument("--right-fill-type", choices=["gradient", "flag-svg"], default="gradient", help="Fill type for right leaf. Default: gradient.")
    parser.add_argument("--right-direction", choices=["horizontal", "vertical"], default="horizontal", help="Gradient direction for right leaf. Default: horizontal.")
    
    args = parser.parse_args()

    input_svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg id="Layer_2" data-name="Layer 2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 633.54 506.72">
  <defs>
    <style>
      .cls-1 { fill: #088180; }
      .cls-1, .cls-2 { stroke-width: 0px; }
      .cls-2 { fill: #fff; }
    </style>
  </defs>
  <g id="Layer_1-2" data-name="Layer 1">
    <path class="cls-1" d="m200.76,164.31s0,.02-.01.04c.01-.02.01-.03.01-.04Z"/>
    <path class="cls-1" d="m336.98,299.22s-.03.01-.04.02c.02-.01.03-.01.04-.02Z"/>
    <path class="cls-2" d="m335.97,494.14c2.17,4.26.47,9.47-3.78,11.64-4.27,2.17-9.48.47-11.64-3.79-2.17-4.27-.49-9.47,3.79-11.63,4.26-2.17,9.47-.47,11.63,3.78Z"/>
    <path class="cls-2" d="m92.66,263.59c23.4,46.34,57.14,86.7,98.33,117.92,30.62-17.89,50.22-52.01,47.69-89.8-2.04-30.52-18.07-56.76-41.39-72.92-7.45-5.16-15.62-9.29-24.34-12.22-3.41-1.13-6.91-2.08-10.47-2.83-42.4-13.57-75.36-49.41-84.13-94.6l-.14-.1C27.48,144.39-4.01,204.67.41,270.87c3.66,54.84,31.24,102.41,71.85,133.18-.18-.14-.34-.28-.52-.42,14.29,11.07,33.1,16.81,52.58,15.51,23.41-1.57,43.64-13.48,56.61-30.95-38.23-34.09-68.6-76.67-88.27-124.61Zm-35.79,124.1s.01.02.03.03t-.03-.03Z"/>
    <path class="cls-2" d="m284.59,97c-12.86,39.08-16.58,80.63-10.99,121.21,27.19,7.15,57.32-1,77.07-23.6,15.96-18.25,21.7-41.94,17.67-64.09-1.28-7.07-3.54-13.98-6.8-20.49-1.27-2.55-2.69-5.03-4.27-7.46-16.16-31.37-14.56-69.93,5.86-100.17v-.14c-48.26-8.63-99.72,7.51-134.33,47.09-28.7,32.81-39.9,74.91-34.39,114.94-.02-.18-.04-.35-.05-.52,1.8,14.22,9.12,27.98,20.78,38.16,14,12.25,32,16.92,49.07,14.38-2.3-40.53,4.54-81.42,20.38-119.31Zm-89.63,49.5s0,.02-.02.04c.02-.02.02-.03.02-.04Z"/>
    <path class="cls-2" d="m465.83,320.23c-50.27,25.39-94.07,62.01-127.93,106.7,19.4,33.22,56.42,54.48,97.43,51.75,33.12-2.21,61.59-19.61,79.13-44.93,5.6-8.07,10.09-16.96,13.25-26.42,1.23-3.7,2.25-7.49,3.08-11.35,14.72-46,53.61-81.77,102.64-91.29l.12-.13c-38.36-55.05-103.77-89.23-175.59-84.43-59.53,3.97-111.13,33.87-144.53,77.94.15-.19.31-.36.46-.55-12.02,15.51-18.24,35.91-16.82,57.05,1.68,25.4,14.61,47.35,33.56,61.42,37-41.46,83.2-74.42,135.21-95.77Zm-134.66-38.82s-.02,0-.02.02c0-.02.01-.02.02-.02Z"/>
    <path class="cls-2" d="m269.5,241.69c-.11.05-.23.11-.35.17-1.69,5.97-3.23,12.03-4.57,18.18-18.98,87.93,3.98,175.16,55.42,240.84,5.66-1.54,11.11-3.67,16.27-6.28-53.72-69.9-79.88-160.26-66.77-252.92Z"/>
    <path class="cls-2" d="m192.17,390.42c-.03.13-.04.28-.06.41,4.35,4.94,8.88,9.79,13.59,14.52,30.01,29.98,64.64,52.48,101.6,67.51-4.39-6.59-8.54-13.37-12.42-20.29-36.69-14.44-71.5-35.14-102.72-62.16Z"/>
  </g>
</svg>
"""
    try:
        root = ET.fromstring(input_svg_content)
    except ET.ParseError as e:
        print(f"Fatal Error: Could not parse input SVG string: {e}")
        exit(1)

    defs_element = root.find(f".//{{{SVG_NAMESPACE}}}defs")
    if defs_element is None: defs_element = ET.SubElement(root, f"{{{SVG_NAMESPACE}}}defs")
    
    layer_group = root.find(f".//{{{SVG_NAMESPACE}}}g[@id='Layer_1-2']")
    if layer_group is None:
        print("Fatal Error: Main layer group 'Layer_1-2' not found in SVG.")
        exit(1)

    processed_paths_list = [] # To avoid processing the same leaf twice

    # Process Top Leaf
    if args.top_country:
        print(f"--- Processing Top Leaf for {args.top_country.upper()} ---")
        top_leaf_params = {
            'country_code': args.top_country.lower(),
            'fill_type': args.top_fill_type,
            'direction': args.top_direction,
            'leaf_name': 'Top'
        }
        # Identification for Top Leaf (specific D, then fallback to min Y)
        top_leaf_id_method = {'type': 'specific_d', 'd_start': "m284.59,97c-12.86,39.08-16.58,80.63-10.99,121.21,27.19,7.15,57.32-1,77.07-23.6,15.96-18.25,21.7-41.94,17.67-64.09-1.28-7.07-3.54-13.98-6.8-20.49-1.27-2.55-2.69-5.03-4.27-7.46-16.16-31.37-14.56-69.93,5.86-100.17v-.14c-48.26-8.63-99.72,7.51-134.33,47.09-28.7,32.81-39.9,74.91-34.39,114.94-.02-.18-.04-.35-.05-.52,1.8,14.22,9.12,27.98,20.78,38.16,14,12.25,32,16.92,49.07,14.38-2.3-40.53,4.54-81.42,20.38-119.31Zm-89.63,49.5s0,.02-.02.04c.02-.02.02-.03.02-.04Z", 'processed_paths': processed_paths_list}
        # If specific_d fails, modify_leaf_fill's internal logic will try a y_coord based on this structure
        # for a more generic 'top' definition if specific 'd_start' isn't found.
        # Or, be more explicit: top_leaf_id_method = {'type': 'y_coord', 'class_filter': 'cls-2', 'select': 'min_y', 'processed_paths': processed_paths_list}
        
        modify_leaf_fill(root, defs_element, layer_group, top_leaf_id_method, top_leaf_params)
    
    # Process Right Leaf
    if args.right_country:
        print(f"--- Processing Right Leaf for {args.right_country.upper()} ---")
        right_leaf_params = {
            'country_code': args.right_country.lower(),
            'fill_type': args.right_fill_type,
            'direction': args.right_direction,
            'leaf_name': 'Right'
        }
        # Identification for Right Leaf (specific D, then fallback to a geometric, e.g. max X)
        # For your SVG, the right leaf is d="m465.83,320.23c..."
        right_leaf_id_method = {'type': 'specific_d', 'd_start': "m465.83,320.23c-50.27,25.39-94.07,62.01-127.93,106.7,19.4,33.22,56.42,54.48,97.43,51.75,33.12-2.21,61.59-19.61,79.13-44.93,5.6-8.07,10.09-16.96,13.25-26.42,1.23-3.7,2.25-7.49,3.08-11.35,14.72-46,53.61-81.77,102.64-91.29l.12-.13c-38.36-55.05-103.77-89.23-175.59-84.43-59.53,3.97-111.13,33.87-144.53,77.94.15-.19.31-.36.46-.55-12.02,15.51-18.24,35.91-16.82,57.05,1.68,25.4,14.61,47.35,33.56,61.42,37-41.46,83.2-74.42,135.21-95.77Zm-134.66-38.82s-.02,0-.02.02c0-.02.01-.02.02-.02Z", 'processed_paths': processed_paths_list}
        # Fallback if specific_d fails for right leaf could be:
        # right_leaf_id_method = {'type': 'geometric', 'class_filter': 'cls-2', 'select': 'max_x_center', 'processed_paths': processed_paths_list}
        
        modify_leaf_fill(root, defs_element, layer_group, right_leaf_id_method, right_leaf_params)

    modified_svg_content = ET.tostring(root, encoding="unicode", method="xml")
    
    # Determine a combined filename if multiple countries, or stick to one if only one is processed
    output_code_parts = []
    if args.top_country: output_code_parts.append(args.top_country)
    if args.right_country: output_code_parts.append(args.right_country)
    
    if not output_code_parts: # No processing done
        print("No country specified for processing. Exiting.")
        exit(0)
        
    output_file_code_tag = "_".join(sorted(list(set(output_code_parts)))) # e.g., cz, or cz_fr
    # Use fill types in filename too if they differ or are flag-svg
    fill_type_tag_parts = []
    if args.top_country: fill_type_tag_parts.append(f"top-{args.top_fill_type}")
    if args.right_country: fill_type_tag_parts.append(f"right-{args.right_fill_type}")
    fill_type_filename_tag = "_".join(fill_type_tag_parts) if fill_type_tag_parts else "defaultfill"


    output_svg_filename = f"modified_logo_{output_file_code_tag}_{fill_type_filename_tag}.svg"
    output_image_filename_base = f"logo_{output_file_code_tag}_{fill_type_filename_tag}"

    with open(output_svg_filename, "w", encoding="utf-8") as f:
        f.write(modified_svg_content)
    print(f"\nSaved modified SVG to: {output_svg_filename}")

    if cairosvg:
        output_image_filename = f"{output_image_filename_base}.png"
        try:
            svg_bytes = modified_svg_content.encode('utf-8')
            cairosvg.svg2png(bytestring=svg_bytes, write_to=output_image_filename, output_width=800)
            print(f"Successfully generated image: {output_image_filename}")
        except Exception as e:
            print(f"Error converting SVG to PNG: {e}")
    elif not cairosvg:
         pass 
    
    print("Processing complete.")