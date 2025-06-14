#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# svg_styler_cli.py

import json
import argparse
import os
from svg_styler_core import generate_and_save_logo, COUNTRY_CODES, create_argument_parser

def run_bulk_generation(args):
    """Handles the logic for generating all logos from presets."""
    output_dir = args.output
    print(f"--- Starting Bulk Generation (Output Directory: {output_dir}) ---")

    try:
        os.makedirs(output_dir, exist_ok=True)
        with open('presets.json', 'r') as f:
            presets = json.load(f)
    except FileNotFoundError:
        print("Error: presets.json not found. Cannot run bulk generation.")
        return
    except json.JSONDecodeError:
        print("Error: Could not parse presets.json. Please check its syntax.")
        return

    for preset_name, config in presets.items():
        print(f"\n--- Processing Preset: {preset_name} ---")
        output_path = os.path.join(output_dir, preset_name)

        # Build params for each leaf from the preset config
        top_params, right_params, left_params = None, None, None

        if 'top_country' in config and config['top_country'] in COUNTRY_CODES:
            top_params = {
                'leaf_name': 'Top',
                'country_code': COUNTRY_CODES[config['top_country']],
                'fill_type': config.get('top_fill_type', 'gradient'),
                'direction': config.get('top_direction', 'horizontal'),
                'transition': config.get('top_transition', 20.0),
                'zoom': config.get('top_zoom', 100.0),
                'pan_x': config.get('top_pan_x', 0.0),
                'pan_y': config.get('top_pan_y', 0.0)
            }

        if 'right_country' in config and config['right_country'] in COUNTRY_CODES:
            right_params = {
                'leaf_name': 'Right',
                'country_code': COUNTRY_CODES[config['right_country']],
                'fill_type': config.get('right_fill_type', 'gradient'),
                'direction': config.get('right_direction', 'horizontal'),
                'transition': config.get('right_transition', 20.0),
                'zoom': config.get('right_zoom', 100.0),
                'pan_x': config.get('right_pan_x', 0.0),
                'pan_y': config.get('right_pan_y', 0.0)
            }
            
        if 'left_country' in config and config['left_country'] in COUNTRY_CODES:
            left_params = {
                'leaf_name': 'Left',
                'country_code': COUNTRY_CODES[config['left_country']],
                'fill_type': config.get('left_fill_type', 'gradient'),
                'direction': config.get('left_direction', 'horizontal'),
                'transition': config.get('left_transition', 20.0),
                'zoom': config.get('left_zoom', 100.0),
                'pan_x': config.get('left_pan_x', 0.0),
                'pan_y': config.get('left_pan_y', 0.0)
            }

        generate_and_save_logo(output_path, top_params=top_params, right_params=right_params, left_params=left_params, png_width=args.png_width)
    
    print("\n--- Bulk Generation Complete ---")


def run_single_generation(parser, initial_args):
    """Handles the logic for generating a single logo."""
    args = initial_args
    # Apply preset defaults if provided
    if args.preset:
        try:
            with open('presets.json', 'r') as f:
                presets = json.load(f)
            
            preset_config = presets.get(args.preset)
            if preset_config:
                print(f"Applying preset '{args.preset}'...")
                parser.set_defaults(**preset_config)
                # Reparse arguments to apply defaults and allow overrides
                args = parser.parse_args()
            else:
                print(f"Warning: Preset '{args.preset}' not found in presets.json. Ignoring.")
        except FileNotFoundError:
            print("Warning: presets.json file not found. Cannot apply preset.")
        except json.JSONDecodeError:
            print("Warning: Could not parse presets.json. Check for syntax errors.")

    top_params, right_params, left_params = None, None, None
    if args.top_country:
        if args.top_country not in COUNTRY_CODES:
            parser.error(f"--top-country '{args.top_country}' is not a valid country name.")
        top_params = {
            'leaf_name': 'Top', 'country_code': COUNTRY_CODES[args.top_country],
            'fill_type': args.top_fill_type, 'direction': args.top_direction,
            'transition': args.top_transition, 'zoom': args.top_zoom,
            'pan_x': args.top_pan_x, 'pan_y': args.top_pan_y
        }

    if args.right_country:
        if args.right_country not in COUNTRY_CODES:
            parser.error(f"--right-country '{args.right_country}' is not a valid country name.")
        right_params = {
            'leaf_name': 'Right', 'country_code': COUNTRY_CODES[args.right_country],
            'fill_type': args.right_fill_type, 'direction': args.right_direction,
            'transition': args.right_transition, 'zoom': args.right_zoom,
            'pan_x': args.right_pan_x, 'pan_y': args.right_pan_y
        }
    
    if args.left_country:
        if args.left_country not in COUNTRY_CODES:
            parser.error(f"--left-country '{args.left_country}' is not a valid country name.")
        left_params = {
            'leaf_name': 'Left', 'country_code': COUNTRY_CODES[args.left_country],
            'fill_type': args.left_fill_type, 'direction': args.left_direction,
            'transition': args.left_transition, 'zoom': args.left_zoom,
            'pan_x': args.left_pan_x, 'pan_y': args.left_pan_y
        }

    if not top_params and not right_params and not left_params:
        parser.error("At least one leaf must be configured. Use a preset or specify a country (e.g., --top-country).")

    generate_and_save_logo(args.output, top_params=top_params, right_params=right_params, left_params=left_params, png_width=args.png_width)

def main():
    parser = create_argument_parser(is_cli=True)
    args = parser.parse_args()

    if args.generate_all:
        run_bulk_generation(args)
    else:
        run_single_generation(parser, args)

if __name__ == "__main__":
    main()