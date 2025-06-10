import math
from PIL import Image

# --- Configuration ---
IMAGE_WIDTH = 1024
IMAGE_HEIGHT = 1024
FILENAME = "circular_gradient.png"

# Define the colors for the gradient in Hex format
# The gradient will go from COLOR_1 (center) -> COLOR_2 (middle) -> COLOR_3 (edge)
COLOR_1_HEX = "20232A"
COLOR_2_HEX = "00695C"
COLOR_3_HEX = "004D40"

# --- Helper Function ---
def hex_to_rgb(hex_color):
    """Converts a hex color string to an (R, G, B) tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# --- Main Logic ---
def create_circular_gradient():
    """
    Generates a 1024x1024 PNG image with a circular gradient of three colors.
    """
    # Convert hex colors to RGB tuples
    color1_rgb = hex_to_rgb(COLOR_1_HEX)
    color2_rgb = hex_to_rgb(COLOR_2_HEX)
    color3_rgb = hex_to_rgb(COLOR_3_HEX)

    # Create a new blank image in RGB mode
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))
    pixels = image.load()

    # Define the center of the image
    center_x = IMAGE_WIDTH / 2
    center_y = IMAGE_HEIGHT / 2

    # Calculate the maximum possible distance from the center (to a corner)
    # This is used to normalize the distance for any pixel to a 0.0-1.0 range
    max_distance = math.sqrt(center_x**2 + center_y**2)

    print("Generating image pixels...")

    # Iterate over every pixel
    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            # Calculate the distance of the pixel from the center
            distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)

            # Normalize the distance to a value between 0.0 and 1.0
            ratio = distance / max_distance

            # --- Interpolate between the three colors ---
            # This logic splits the gradient into two parts:
            # 1. From the center (0.0) to the midpoint (0.5), interpolate between COLOR_1 and COLOR_2.
            # 2. From the midpoint (0.5) to the edge (1.0), interpolate between COLOR_2 and COLOR_3.

            if ratio < 0.5:
                # We are in the first half of the gradient
                # Re-normalize the ratio for this segment (0.0 to 1.0)
                segment_ratio = ratio / 0.5
                start_color = color1_rgb
                end_color = color2_rgb
            else:
                # We are in the second half of the gradient
                # Re-normalize the ratio for this segment (0.0 to 1.0)
                segment_ratio = (ratio - 0.5) / 0.5
                start_color = color2_rgb
                end_color = color3_rgb
            
            # Linear interpolation (lerp) for each color channel
            r = int(start_color[0] * (1 - segment_ratio) + end_color[0] * segment_ratio)
            g = int(start_color[1] * (1 - segment_ratio) + end_color[1] * segment_ratio)
            b = int(start_color[2] * (1 - segment_ratio) + end_color[2] * segment_ratio)

            # Assign the calculated color to the pixel
            pixels[x, y] = (r, g, b)

    # Save the final image
    try:
        image.save(FILENAME)
        print(f"\nSuccessfully created '{FILENAME}' ({IMAGE_WIDTH}x{IMAGE_HEIGHT})")
    except Exception as e:
        print(f"Error saving file: {e}")

# --- Run the script ---
if __name__ == "__main__":
    create_circular_gradient()
