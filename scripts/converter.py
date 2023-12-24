from pathlib import Path
from PIL import Image
from itertools import chain

def convert_to_webp(source):
    """Convert image to webp.

    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


def main():
    png_images = Path("./downloaded_images").glob("**/*.png")
    jpg_images = Path("./downloaded_images").glob("**/*.jpg")
    jpeg_images = Path("./downloaded_images").glob("**/*.jpeg")
    
    for path in png_images:
        webp_path = convert_to_webp(path)
        print(webp_path)
    
    for path in jpg_images:
        webp_path = convert_to_webp(path)
        print(webp_path)

    for path in jpeg_images:
        webp_path = convert_to_webp(path)
        print(webp_path)

if __name__ == '__main__':
    main()