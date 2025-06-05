#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import re
import os
import argparse
import uuid

# ... (CairoSVG and country_data imports remain the same) ...
try:
    import cairosvg
except ImportError:
    print("DEBUG: CairoSVG import failed or not found.") # More visible debug
    cairosvg = None
else:
    print("DEBUG: CairoSVG imported successfully.")


try:
    from country_data import COUNTRY_COLORS, COUNTRY_CODES
except ImportError:
    print("Error: Could not import from country_data.py.")
    print("Please ensure 'country_data.py' exists in the same directory as this script.")
    exit(1)

SVG_NAMESPACE = "http://www.w3.org/2000/svg"
ET.register_namespace('', SVG_NAMESPACE)
ET.register_namespace('xlink', "http://www.w3.org/1999/xlink")

CODE_TO_COUNTRY_NAME = {code: name for name, code in COUNTRY_CODES.items()}

# --- Helper Functions ---
def get_initial_y_from_d(d_attr):
    if not d_attr: return None
    # Regex to find the first moveto command (M or m) and capture Y
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
        print(f"Warning: Flag SVG not found at '{flag_svg_path}'. Cannot create pattern.")
        return None
    try:
        flag_tree = ET.parse(flag_svg_path)
        flag_root = flag_tree.getroot()
    except Exception as e:
        print(f"Warning: Could not load/parse flag SVG '{flag_svg_path}': {e}. Cannot create pattern.")
        return None

    existing_pattern = defs_element.find(f".//{{{SVG_NAMESPACE}}}pattern[@id='{pattern_id}']")
    if existing_pattern is not None: defs_element.remove(existing_pattern)

    flag_viewbox = flag_root.get("viewBox", "0 0 100 100")
    vb_parts = flag_viewbox.split()
    p_width = flag_root.get("width", vb_parts[2] if len(vb_parts) == 4 else "100")
    p_height = flag_root.get("height", vb_parts[3] if len(vb_parts) == 4 else "100")

    pattern_attribs = {
        "id": pattern_id, "patternUnits": "userSpaceOnUse",
        "width": p_width, "height": p_height,
        "viewBox": flag_viewbox, "preserveAspectRatio": "xMidYMid slice"
    }
    pattern_element = ET.SubElement(defs_element, f"{{{SVG_NAMESPACE}}}pattern", pattern_attribs)
    for child in flag_root:
        if child.tag.split('}')[-1] not in ["defs", "style", "metadata", "title", "desc", "sodipodi:namedview", "inkscape:perspective"]: # Added more Inkscape/Sodipodi specific tags to ignore
            pattern_element.append(child)
    return pattern_id


def get_simple_path_bbox(d_attr):
    if not d_attr: return None
    points_x = []
    points_y = []
    
    # More robust regex to find numbers, including scientific notation and handling leading commands
    # This will try to find all coordinate pairs following commands.
    # It's still not a full parser but better than just finding numbers.
    path_commands = re.findall(r"([mMlLhHvVcCsSqQtTaAzZ])([^mMlLhHvVcCsSqQtTaAzZ]*)", d_attr)
    
    current_x, current_y = 0, 0
    
    for cmd, params_str in path_commands:
        params = [float(p) for p in re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", params_str)]
        
        idx = 0
        is_relative = cmd.islower()
        cmd_upper = cmd.upper()

        if cmd_upper == 'M': # Moveto
            while idx < len(params):
                px = params[idx] + (current_x if is_relative and points_x else 0)
                py = params[idx+1] + (current_y if is_relative and points_y else 0)
                points_x.append(px)
                points_y.append(py)
                current_x, current_y = px, py
                idx += 2
                if cmd_upper == 'M': cmd_upper = 'L' # Subsequent pairs for M are L
        elif cmd_upper == 'L': # Lineto
             while idx < len(params):
                px = params[idx] + (current_x if is_relative else 0)
                py = params[idx+1] + (current_y if is_relative else 0)
                points_x.append(px)
                points_y.append(py)
                current_x, current_y = px, py
                idx += 2
        elif cmd_upper == 'H': # Horizontal lineto
            while idx < len(params):
                px = params[idx] + (current_x if is_relative else 0)
                py = current_y
                points_x.append(px)
                points_y.append(py)
                current_x = px
                idx += 1
        elif cmd_upper == 'V': # Vertical lineto
            while idx < len(params):
                px = current_x
                py = params[idx] + (current_y if is_relative else 0)
                points_x.append(px)
                points_y.append(py)
                current_y = py
                idx += 1
        elif cmd_upper in ['C', 'S', 'Q', 'T', 'A']: # Curves - just take end points for this simple bbox
            # For C: x1 y1 x2 y2 x y (take x,y)
            # For S: x2 y2 x y (take x,y)
            # For Q: x1 y1 x y (take x,y)
            # For T: x y (take x,y)
            # For A: ... x y (take x,y)
            num_coords_per_segment_end = 2 
            if cmd_upper == 'C': num_params_per_segment = 6
            elif cmd_upper == 'S': num_params_per_segment = 4
            elif cmd_upper == 'Q': num_params_per_segment = 4
            elif cmd_upper == 'T': num_params_per_segment = 2
            elif cmd_upper == 'A': num_params_per_segment = 7 # rx ry x-axis-rotation large-arc-flag sweep-flag x y
            else: continue

            while idx + num_params_per_segment <= len(params):
                end_point_idx_offset = num_params_per_segment - num_coords_per_segment_end
                px = params[idx + end_point_idx_offset] + (current_x if is_relative else 0)
                py = params[idx + end_point_idx_offset + 1] + (current_y if is_relative else 0)
                points_x.append(px)
                points_y.append(py)
                current_x, current_y = px, py
                idx += num_params_per_segment
        elif cmd_upper == 'Z': # Close path
            if points_x: # Go back to the first point of the current subpath
                # This doesn't add new points to bbox, just closes the shape
                pass 
    
    if not points_x or not points_y:
        # Fallback if no points extracted (e.g., malformed path or only Z)
        print("Warning: BBox calculation could not extract points from path. Using default small bbox.")
        return {"x": 0, "y": 0, "width": 1, "height": 1}

    min_x, max_x = min(points_x), max(points_x)
    min_y, max_y = min(points_y), max(points_y)
    
    return {
        "x": min_x, "y": min_y, 
        "width": max_x - min_x if max_x > min_x else 1,
        "height": max_y - min_y if max_y > min_y else 1
    }

def apply_fill_to_leaf(svg_string, country_name, country_code, fill_type="gradient", gradient_direction="horizontal"):
    print(f"DEBUG: apply_fill_to_leaf called for {country_name}, code: {country_code}, fill: {fill_type}, dir: {gradient_direction}")
    if country_name not in COUNTRY_COLORS:
        print(f"Error: Data for country '{country_name}' (code: {country_code}) not defined.")
        return None

    try:
        root = ET.fromstring(svg_string)
    except ET.ParseError as e:
        print(f"Error parsing main SVG: {e}")
        return None

    defs_element = root.find(f".//{{{SVG_NAMESPACE}}}defs")
    if defs_element is None:
        defs_element = ET.SubElement(root, f"{{{SVG_NAMESPACE}}}defs")
        print("DEBUG: Created <defs> element.")

    pattern_id_base = f"{country_code}-leaf-{uuid.uuid4().hex[:4]}"

    # --- Identify target leaf ---
    target_path_element = None
    target_path_index = -1 # Store index for replacement
    identified_by = "None" # Initialize

    # Ensure this group ID matches your SVG structure
    layer_group_id = "Layer_1-2" 
    layer_group = root.find(f".//{{{SVG_NAMESPACE}}}g[@id='{layer_group_id}']") 

    if layer_group is None:
        print(f"Error: Could not find the layer group '{layer_group_id}'. Please check main SVG structure.")
        # Fallback: search for the path anywhere in the SVG (less ideal)
        # layer_group = root 
        # print(f"DEBUG: Searching for path in root due to missing '{layer_group_id}'.")
        return ET.tostring(root, encoding="unicode", method="xml") # Early exit if group is essential

    print(f"DEBUG: Found group '{layer_group_id}'. Number of children: {len(list(layer_group))}")

    # Path identification strategy:
    # 1. Try specific 'd' attribute start (most reliable if known and stable).
    # 2. Fallback: Iterate cls-2 paths, pick one with smallest Y (original logic).
    # 3. Ultimate Fallback: If no cls-2, iterate *all* paths in the group and pick smallest Y.
    
    # Strategy 1: Specific d-attribute
    specific_d_start_leaf = "m284.59,97c" # The "top leaf" d-attribute start
    
    all_paths_in_group = [el for el in list(layer_group) if el.tag == f"{{{SVG_NAMESPACE}}}path"]
    print(f"DEBUG: Total paths found in '{layer_group_id}': {len(all_paths_in_group)}")
    
    for i, path_el in enumerate(all_paths_in_group):
        path_d = path_el.get("d", "")
        # print(f"DEBUG: Checking path {i} with d starting: {path_d[:20]}...") # Verbose
        if path_d.strip().startswith(specific_d_start_leaf):
            target_path_element = path_el
            identified_by = f"specific d-attribute '{specific_d_start_leaf}...'"
            target_path_index = layer_group.getchildren().index(path_el) if hasattr(layer_group, 'getchildren') else list(layer_group).index(path_el)
            print(f"DEBUG: Leaf found by specific 'd' at index {target_path_index}.")
            break
    
    # Strategy 2 & 3: Fallback to class or general Y-coordinate
    if not target_path_element:
        print(f"DEBUG: Leaf not found by specific 'd'. Trying class/Y-coordinate method.")
        min_y = float('inf')
        
        candidate_paths_for_y_check = []
        cls2_paths = [p for p in all_paths_in_group if p.get("class") == "cls-2"]

        if cls2_paths:
            print(f"DEBUG: Found {len(cls2_paths)} paths with class 'cls-2'.")
            candidate_paths_for_y_check = cls2_paths
            id_method_prefix = "cls-2 path with "
        else:
            print("DEBUG: No 'cls-2' paths found. Checking all paths in group for min Y.")
            candidate_paths_for_y_check = all_paths_in_group
            id_method_prefix = "any path with "

        if not candidate_paths_for_y_check:
            print("DEBUG: No candidate paths found at all for Y-coordinate check.")

        for path_el in candidate_paths_for_y_check:
            path_d = path_el.get("d", "")
            y_coord = get_initial_y_from_d(path_d)
            if y_coord is not None:
                # print(f"DEBUG: Path with Y={y_coord:.2f}, current min_y={min_y:.2f}") # Verbose
                if y_coord < min_y:
                    min_y = y_coord
                    target_path_element = path_el
                    identified_by = f"{id_method_prefix}min Y-coordinate ({min_y:.2f})"
                    target_path_index = list(layer_group).index(path_el)
        if target_path_element:
             print(f"DEBUG: Leaf found by Y-coordinate method at index {target_path_index}.")


    if not target_path_element:
        print(f"Error: Could not identify the target 'top leaf' path using any method. Identified_by: {identified_by}")
        return ET.tostring(root, encoding="unicode", method="xml")

    print(f"DEBUG: Successfully identified target leaf. Method: {identified_by}")
    leaf_d_attribute = target_path_element.get("d")
    if not leaf_d_attribute:
        print("Error: Target leaf path has no 'd' attribute. This should not happen if path was identified.")
        return ET.tostring(root, encoding="unicode", method="xml")

    # --- Apply chosen fill type ---
    fill_applied_successfully = False # Flag to track if flag-svg fill worked

    if fill_type == "flag-svg":
        print(f"Info: Attempting to use flag SVG with clip-path for {country_name}.")
        pattern_id = create_flag_pattern_definition(defs_element, country_code, pattern_id_base)
        
        if pattern_id:
            clip_path_id = f"clip-{pattern_id_base}-{uuid.uuid4().hex[:6]}"
            
            clip_path_el = ET.SubElement(defs_element, f"{{{SVG_NAMESPACE}}}clipPath", {"id": clip_path_id})
            ET.SubElement(clip_path_el, f"{{{SVG_NAMESPACE}}}path", {"d": leaf_d_attribute, "fill":"#000000"}) # Fill for clipPath path is irrelevant but some renderers might need it
            
            bbox = get_simple_path_bbox(leaf_d_attribute) 
            if not bbox: 
                print("Warning: Could not calculate bounding box for leaf. Using default rect size for flag pattern.")
                # A more robust fallback might be needed if bbox is crucial and often fails
                # For now, let's assume the pattern's own preserveAspectRatio will handle it mostly
                bbox_attrs = {"width": "100%", "height": "100%", "x": "0", "y": "0"} # Relative to viewport
            else:
                bbox_attrs = {"x": str(bbox['x']), "y": str(bbox['y']), "width": str(bbox['width']), "height": str(bbox['height'])}


            clipped_group = ET.Element(f"{{{SVG_NAMESPACE}}}g", {"clip-path": f"url(#{clip_path_id})"})
            ET.SubElement(clipped_group, f"{{{SVG_NAMESPACE}}}rect", {**bbox_attrs, "fill": f"url(#{pattern_id})"})
            
            # Structural change: replace path with group
            print(f"DEBUG: Replacing original path at index {target_path_index} with new clipped group.")
            layer_group.remove(target_path_element) 
            layer_group.insert(target_path_index, clipped_group)

            print(f"Info: Applied flag SVG pattern for {country_name} using clip-path '{clip_path_id}'.")
            fill_applied_successfully = True
        else: 
            print(f"Warning: Flag SVG pattern creation failed for {country_code}. Falling back to gradient.")
            fill_applied_successfully = False # Explicitly set


    # Fallback to gradient or if explicitly chosen
    # If flag-svg was chosen but failed, target_path_element is still the original path (it wasn't replaced)
    # If flag-svg succeeded, target_path_element was removed, so this block shouldn't try to set its fill.
    if fill_type == "gradient" or (fill_type == "flag-svg" and not fill_applied_successfully):
        if target_path_element.getparent() is None and fill_type == "flag-svg" and not fill_applied_successfully:
             print("DEBUG: Original target path seems to have been detached unexpectedly during a failed flag-svg attempt. This indicates a logic flaw.")
             # This state should not be reached if replacement logic is correct
        else:
            colors = COUNTRY_COLORS[country_name]
            gradient_id = create_gradient_definition(defs_element, colors, pattern_id_base, gradient_direction)
            # Ensure target_path_element is still valid before setting fill
            # This is crucial if it might have been removed by a failed flag-svg attempt that partially modified the tree
            if target_path_element.getparent() is not None: # Check if it's still in the tree
                target_path_element.set("fill", f"url(#{gradient_id})")
                if 'class' in target_path_element.attrib:
                    target_path_element.attrib.pop('class')
                print(f"Info: Applied {gradient_direction} gradient for {country_name} (Identified by: {identified_by}).")
            else:
                print("ERROR: Target path for gradient fill was unexpectedly removed from the SVG tree. Gradient not applied.")


    return ET.tostring(root, encoding="unicode", method="xml")


# --- Main execution ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Apply a country's flag (gradient or SVG pattern) to an SVG leaf and export.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("country_code", 
                        help="The 2-letter country code (e.g., fr, de, us).",
                        choices=CODE_TO_COUNTRY_NAME.keys(), 
                        metavar="CountryCode" 
                        )
    parser.add_argument("--fill-type",
                        choices=["gradient", "flag-svg"],
                        default="gradient",
                        help="Type of fill for the leaf.\n"
                             "  gradient: Uses flag colors to create a linear gradient.\n"
                             "  flag-svg: Attempts to use the flag's SVG file as a clipped pattern fill.\n"
                             "            (Requires flag SVGs in 'flags/{CountryCode}.svg')\n"
                             "Default: gradient."
                        )
    parser.add_argument("--direction",
                        choices=["horizontal", "vertical"],
                        default="horizontal",
                        help="Gradient direction (if fill-type is gradient). Default: horizontal."
                        )
    
    args = parser.parse_args()
    chosen_country_code = args.country_code.lower()
    fill_type = args.fill_type
    gradient_direction = args.direction.lower()

    chosen_country_name = CODE_TO_COUNTRY_NAME.get(chosen_country_code)

    if not chosen_country_name:
        print(f"Error: Country code '{chosen_country_code}' is not recognized.")
        exit(1)

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

    print(f"--- Processing SVG for {chosen_country_name} (code: {chosen_country_code}) with {fill_type} ---")
    modified_svg_content = apply_fill_to_leaf(
        input_svg_content, 
        chosen_country_name, 
        chosen_country_code,
        fill_type=fill_type,
        gradient_direction=gradient_direction
    )

    if modified_svg_content:
        output_svg_filename = f"modified_logo_{chosen_country_code}_{fill_type}.svg"
        output_image_filename_base = f"logo_{chosen_country_code}_{fill_type}"

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
             pass # Message already printed
    else:
        print(f"\nSVG modification failed for {chosen_country_name}. No output generated.")
        exit(1)