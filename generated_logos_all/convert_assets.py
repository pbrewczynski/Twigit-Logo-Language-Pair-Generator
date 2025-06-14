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
      "filename": "" # To be filled by the script
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
      "filename": "" # To be filled by the script
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

def create_imageset(base_name, source_file_name, is_vector, output_dir):
    """
    Creates an .imageset directory in the specified output directory, copies the
    source file, and writes the correct Contents.json file.
    
    Args:
        base_name (str): The base name for the imageset (e.g., 'en-pl').
        source_file_name (str): The name of the source file (e.g., 'en-pl.svg').
        is_vector (bool): True if the source is a vector asset (SVG/PDF).
        output_dir (str): The directory where the .imageset folder will be created.
    """
    imageset_full_path = os.path.join(output_dir, f"{base_name}.imageset")
    
    # Create the .imageset directory
    os.makedirs(imageset_full_path, exist_ok=True)
    
    # Copy the source file into the new directory. The source is assumed to be in the
    # current working directory from where the script is run.
    shutil.copy(source_file_name, os.path.join(imageset_full_path, source_file_name))
    
    # Select and configure the correct JSON template
    json_content = CONTENTS_JSON_VECTOR if is_vector else CONTENTS_JSON_RASTER
    json_content["images"][0]["filename"] = source_file_name
    
    # Write the Contents.json file
    json_path = os.path.join(imageset_full_path, "Contents.json")
    with open(json_path, 'w') as f:
        json.dump(json_content, f, indent=2)
        
    print(f"  -> Created {os.path.relpath(imageset_full_path)}")

def main():
    """
    Scans the current directory for assets named like 'xx-yy.ext' and
    generates Xcode .imageset bundles in a specified output directory.
    """
    parser = argparse.ArgumentParser(
        description="Scans the current directory for language-pair assets and creates Xcode .imageset bundles.",
        formatter_class=argparse.RawTextHelpFormatter # For better help text formatting
    )
    parser.add_argument(
        "-o", "--output",
        help="The path to the output directory where .imageset folders will be created.\nDefaults to the current directory.",
        default='.' # Default to current directory if not specified
    )
    args = parser.parse_args()
    
    source_dir = '.'
    output_dir = args.output
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Starting asset conversion for Xcode...")
    print(f"Scanning for source files in: '{os.path.abspath(source_dir)}'")
    print(f"Output will be saved to: '{os.path.abspath(output_dir)}'")
    
    # Regex to find files with a 'xx-yy' naming convention.
    lang_pair_pattern = re.compile(r'^([a-z]{2,3}-[a-z]{2,3})$')
    
    processed_pairs = set()

    # Iterate over all files in the source directory
    for filename in sorted(os.listdir(source_dir)):
        base_name, _ = os.path.splitext(filename)
        
        # Check if the file's base name matches our pattern (e.g., 'en-pl')
        if lang_pair_pattern.match(base_name) and base_name not in processed_pairs:
            print(f"\nProcessing pair: '{base_name}'")
            
            # --- 1. Handle Vector Asset (.svg or .pdf) ---
            # Xcode prefers vector assets. We prioritize .svg over .pdf.
            vector_source_file = f"{base_name}.svg"
            if not os.path.exists(vector_source_file):
                vector_source_file = f"{base_name}.pdf" # Fallback to .pdf
            
            if os.path.exists(vector_source_file):
                create_imageset(base_name, vector_source_file, is_vector=True, output_dir=output_dir)
            else:
                print(f"  -> No vector file (.svg or .pdf) found for '{base_name}'.")

            # --- 2. Handle Raster Asset (.png) ---
            raster_source_file = f"{base_name}.png"
            if os.path.exists(raster_source_file):
                # The raster version gets a '-raster' suffix for clarity
                raster_imageset_base_name = f"{base_name}-raster"
                create_imageset(raster_imageset_base_name, raster_source_file, is_vector=False, output_dir=output_dir)
            else:
                print(f"  -> No raster file (.png) found for '{base_name}'.")

            # Add to set to avoid processing this pair again
            processed_pairs.add(base_name)

    print("\nAsset conversion finished.")

if __name__ == "__main__":
    main()