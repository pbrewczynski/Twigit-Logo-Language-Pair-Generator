#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# svg_styler_cli.py

# No need for argparse here, it's handled in the core module
from svg_styler_core import generate_and_save_logo, COUNTRY_CODES, create_argument_parser

def main():
    # Get the parser from the core module, configured for CLI usage
    parser = create_argument_parser(is_cli=True)
    args = parser.parse_args()

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

    # The original check for at least one leaf is no longer needed for the CLI,
    # as not providing a country will just generate a logo with default leaves.
    # We can keep it for user-friendliness if desired.
    if not top_params and not right_params and not left_params:
        parser.error("At least one leaf must be configured for the CLI. Use --top-country, --right-country, or --left-country.")

    generate_and_save_logo(args.output, top_params=top_params, right_params=right_params, left_params=left_params, png_width=args.png_width)

if __name__ == "__main__":
    main()