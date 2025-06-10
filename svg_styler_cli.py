#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# svg_styler_cli.py

import argparse
from svg_styler_core import generate_and_save_logo, COUNTRY_CODES

def main():
    parser = argparse.ArgumentParser(
        description="A command-line tool to style an SVG logo with country flags or gradients.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help="Output file path (without extension). e.g., 'my_logo'. Will generate 'my_logo.svg' and 'my_logo.png'."
    )
    parser.add_argument(
        '--png-width',
        type=int,
        default=1200,
        help="Width of the output PNG file in pixels. Default is 1200."
    )

    # --- Top Leaf Arguments ---
    top_group = parser.add_argument_group('Top Leaf Options')
    top_group.add_argument('--top-country', type=str, help='Name of the country for the top leaf. (e.g., "United States")')
    top_group.add_argument('--top-fill-type', choices=['gradient', 'flag-svg'], default='gradient', help='Fill type for the top leaf.')
    top_group.add_argument('--top-direction', choices=['horizontal', 'vertical'], default='horizontal', help='Direction for gradient fill.')
    top_group.add_argument('--top-transition', type=float, default=20.0, help='Transition softness for gradient (1-99).')
    top_group.add_argument('--top-zoom', type=float, default=100.0, help='Zoom level for flag fill (25-400).')
    top_group.add_argument('--top-pan-x', type=float, default=0.0, help='Horizontal pan for flag fill (-100 to 100).')
    top_group.add_argument('--top-pan-y', type=float, default=0.0, help='Vertical pan for flag fill (-100 to 100).')

    # --- Right Leaf Arguments ---
    right_group = parser.add_argument_group('Right Leaf Options')
    right_group.add_argument('--right-country', type=str, help='Name of the country for the right leaf. (e.g., "Germany")')
    right_group.add_argument('--right-fill-type', choices=['gradient', 'flag-svg'], default='gradient', help='Fill type for the right leaf.')
    right_group.add_argument('--right-direction', choices=['horizontal', 'vertical'], default='horizontal', help='Direction for gradient fill.')
    right_group.add_argument('--right-transition', type=float, default=20.0, help='Transition softness for gradient (1-99).')
    right_group.add_argument('--right-zoom', type=float, default=100.0, help='Zoom level for flag fill (25-400).')
    right_group.add_argument('--right-pan-x', type=float, default=0.0, help='Horizontal pan for flag fill (-100 to 100).')
    right_group.add_argument('--right-pan-y', type=float, default=0.0, help='Vertical pan for flag fill (-100 to 100).')

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

    if not top_params and not right_params:
        parser.error("At least one leaf must be configured. Use --top-country or --right-country.")

    generate_and_save_logo(args.output, top_params, right_params, args.png_width)

if __name__ == "__main__":
    main()