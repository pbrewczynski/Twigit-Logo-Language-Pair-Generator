import os
import shutil
import json
import re
import argparse

# JSON template for raster images (e.g., PNG)
CONTENTS_JSON_RASTER = {
  "images": [
    {
      "idiom": "universal",
      "filename": ""
    }
  ],
  "info": {
    "author": "xcode",
    "version": 1
  }
}

# JSON template for vector images (e.g., PDF/SVG)
CONTENTS_JSON_VECTOR = {
  "images": [
    {
      "idiom": "universal",
      "filename": ""
    }
  ],
  "info": {
    "author": "xcode",
    "version": 1
  },
  "properties": {
    "preserves-vector-representation": True
  }
}

def create_imageset(base_name, source_file_path, is_vector, output_dir, verbose=False):
    """
    Creates an .imageset directory, copies the source file, and writes Contents.json.
    """
    imageset_full_path = os.path.join(output_dir, f"{base_name}.imageset")
    source_filename = os.path.basename(source_file_path)

    # Create the .imageset directory
    os.makedirs(imageset_full_path, exist_ok=True)

    # Copy the source file into the new directory
    shutil.copy(source_file_path, os.path.join(imageset_full_path, source_filename))

    # Select and configure the correct JSON template
    json_content = CONTENTS_JSON_VECTOR if is_vector else CONTENTS_JSON_RASTER
    json_content["images"][0]["filename"] = source_filename

    # Write the Contents.json file
    json_path = os.path.join(imageset_full_path, "Contents.json")
    with open(json_path, 'w') as f:
        json.dump(json_content, f, indent=2)
    
    if verbose:
        asset_type = "Vector" if is_vector else "Raster"
        print(f"  -> Created {asset_type} Asset: {os.path.relpath(imageset_full_path)} from {source_filename}")

def main():
    """
    Scans a source directory for assets and generates Xcode .imageset bundles.
    """
    parser = argparse.ArgumentParser(
        description="Scans a source directory for language-pair assets (e.g., 'en-pl.svg') and creates Xcode .imageset bundles.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "-s", "--source",
        default='.',
        help="Path to the source directory containing the raw .svg, .pdf, and .png files.\n(default: current directory)"
    )
    parser.add_argument(
        "-o", "--output",
        default='convert_assets_output', # <-- CHANGED THIS LINE
        help="Path to the output directory where .imageset folders will be created.\n(default: convert_assets_output)" # <-- UPDATED HELP TEXT
    )
    parser.add_argument(
        "--raster-suffix",
        default='-raster',
        help="Suffix to append to raster imagesets when a vector version also exists.\n(default: '-raster')"
    )
    parser.add_argument(
        "--clean",
        action='store_true',
        help="Delete the output directory before generating new assets. Use with caution."
    )
    parser.add_argument(
        "-v", "--verbose",
        action='store_true',
        help="Enable verbose logging to see more details about the process."
    )
    args = parser.parse_args()

    # --- Initial Setup ---
    source_dir = args.source
    output_dir = args.output
    
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory not found at '{source_dir}'")
        return

    print(f"Asset Conversion Started")
    print(f"Source:      '{os.path.abspath(source_dir)}'")
    print(f"Output:      '{os.path.abspath(output_dir)}'")
    if args.clean:
        print("Mode:        Clean build (output directory will be removed)")

    if args.clean and os.path.isdir(output_dir):
        print(f"Cleaning output directory: {output_dir}")
        shutil.rmtree(output_dir)

    os.makedirs(output_dir, exist_ok=True)

    # --- Processing Logic ---
    lang_pair_pattern = re.compile(r'^([a-z]{2,3}-[a-z]{2,3})$')
    processed_pairs = set()

    for filename in sorted(os.listdir(source_dir)):
        base_name, _ = os.path.splitext(filename)
        
        if lang_pair_pattern.match(base_name) and base_name not in processed_pairs:
            print(f"\nProcessing pair: '{base_name}'")
            
            # Check for all possible asset types for this pair
            svg_path = os.path.join(source_dir, f"{base_name}.svg")
            pdf_path = os.path.join(source_dir, f"{base_name}.pdf")
            png_path = os.path.join(source_dir, f"{base_name}.png")
            
            has_svg = os.path.exists(svg_path)
            has_pdf = os.path.exists(pdf_path)
            has_png = os.path.exists(png_path)
            has_vector = has_svg or has_pdf

            # --- Decision Logic ---
            if has_vector:
                # 1. A vector asset exists. Create the primary .imageset from it.
                # Prioritize SVG over PDF.
                vector_source_path = svg_path if has_svg else pdf_path
                create_imageset(base_name, vector_source_path, is_vector=True, output_dir=output_dir, verbose=args.verbose)
                
                # 2. If a PNG also exists, create a separate, suffixed raster set.
                if has_png:
                    raster_imageset_name = f"{base_name}{args.raster_suffix}"
                    create_imageset(raster_imageset_name, png_path, is_vector=False, output_dir=output_dir, verbose=args.verbose)

            elif has_png:
                # 3. No vector, but a PNG exists. Create the primary .imageset from the PNG.
                # It is NOT given the raster suffix in this case.
                create_imageset(base_name, png_path, is_vector=False, output_dir=output_dir, verbose=args.verbose)
            
            else:
                if args.verbose:
                    print(f"  -> No assets (.svg, .pdf, .png) found for '{base_name}', skipping.")

            processed_pairs.add(base_name)

    print("\nAsset conversion finished successfully.")

if __name__ == "__main__":
    main()