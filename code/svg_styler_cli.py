#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# svg_styler_cli.py

import json
import argparse
from svg_styler_core import generate_and_save_logo, COUNTRY_CODES, create_argument_parser

def main():
    # --- Preset Loading Logic ---
    # Create a temporary parser just to find the --preset argument.
    # We use add_help=False to prevent it from printing help and exiting on -h.
    preset_parser = argparse.ArgumentParser(add_help=False)
    preset_parser.add_argument('--preset', type=str)
    # Use parse_known_args to find the preset value and ignore all other args.
    preset_args, _ = preset_parser.parse_known_args()

    preset_config = {}
    if preset_args.preset:
        try:
            # Assumes presets.json is in the same directory as the script.
            with open('presets.json', 'r') as f:
                presets = json.load(f)
            
            preset_data = presets.get(preset_args.preset)
            if preset_data:
                print(f"Applying preset '{preset_args.preset}'...")
                preset_config = preset_data
            else:
                print(f"Warning: Preset '{preset_args.preset}' not found in presets.json. Ignoring.")
        except FileNotFoundError:
            print("Warning: presets.json file not found. Cannot apply preset.")
        except json.JSONDecodeError:
            print("Warning: Could not parse presets.json. Check for syntax errors.")

    # --- Main Argument Parsing ---
    # Get the full parser from the core module.
    parser = create_argument_parser(is_cli=True)

    # Apply the loaded preset configuration as defaults.
    # These will be overridden by any arguments specified on the command line.
    if preset_config:
        parser.set_defaults(**preset_config)

    # Now, parse all arguments fully.
    args = parser.parse_args()

    # The rest of the script continues as before, using the final `args` object.
    top_params = None
    if args.top_country:
        if args.top_country not in COUNTRY_CODES:
            print(f"Error: --top-country '{args.top_country}' is not a valid country name.")
            return
        top_params = {
            'leaf_name': 'Top',
            'country_code': COUNTRY_CODES[args.top_country],
            'fill_type': args.top_fill_type,
            'direction': args.top_direction,
            'transition': args.top_transition,
            'zoom': args.top_zoom,
            'pan_x': args.top_pan_x,
            'pan_y': args.top_pan_y
        }

    right_params = None
    if args.right_country:
        if args.right_country not in COUNTRY_CODES:
            print(f"Error: --right-country '{args.right_country}' is not a valid country name.")
            return
        right_params = {
            'leaf_name': 'Right',
            'country_code': COUNTRY_CODES[args.right_country],
            'fill_type': args.right_fill_type,
            'direction': args.right_direction,
            'transition': args.right_transition,
            'zoom': args.right_zoom,
            'pan_x': args.right_pan_x,
            'pan_y': args.right_pan_y
        }
    
    left_params = None
    if args.left_country:
        if args.left_country not in COUNTRY_CODES:
            print(f"Error: --left-country '{args.left_country}' is not a valid country name.")
            return
        left_params = {
            'leaf_name': 'Left',
            'country_code': COUNTRY_CODES[args.left_country],
            'fill_type': args.left_fill_type,
            'direction': args.left_direction,
            'transition': args.left_transition,
            'zoom': args.left_zoom,
            'pan_x': args.left_pan_x,
            'pan_y': args.left_pan_y
        }

    if not top_params and not right_params and not left_params:
        parser.error("At least one leaf must be configured. Use a preset or specify a country (e.g., --top-country).")

    generate_and_save_logo(args.output, top_params=top_params, right_params=right_params, left_params=left_params, png_width=args.png_width)

if __name__ == "__main__":
    main()