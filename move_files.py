import os
import shutil

def move_webp_files(src_folder, dest_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)

    # List all files in the source folder
    files = os.listdir(src_folder)

    # Filter files with the .webp extension
    webp_files = [file for file in files if file.lower().endswith('.webp')]

    # Move each .webp file to the destination folder
    for webp_file in webp_files:
        src_path = os.path.join(src_folder, webp_file)
        dest_path = os.path.join(dest_folder, webp_file)
        shutil.move(src_path, dest_path)
        print(f"Moved: {webp_file}")

if __name__ == "__main__":
    source_folder = "./downloaded_images"
    destination_folder = "./converted_images"

    move_webp_files(source_folder, destination_folder)
