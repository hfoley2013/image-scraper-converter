from pathlib import Path

def delete_all_images(folder_path):
    folder = Path(folder_path)

    # Iterate over all files in the folder
    for file_path in folder.glob('*'):
        # Check if the file is an image (you can adjust the list of image extensions)
        if file_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp']:
            # Delete the image file
            file_path.unlink()

if __name__ == '__main__':
    folder_paths = [
        "./downloaded_images",
        "./converted_images"
    ]

    for folder_path in folder_paths:
        delete_all_images(folder_path)
