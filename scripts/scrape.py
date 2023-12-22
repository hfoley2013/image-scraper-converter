import os
import requests
from bs4 import BeautifulSoup


def download_images(url, folder):
    print(f"Processing {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags in the HTML
    img_tags = soup.find_all('img')

    print(f"Found {len(img_tags)} images")
    i = 1
    for img_tag in img_tags:
        print(f"Downloading image {i} of {len(img_tags)}")
        # Get the source URL of each image
        img_url = img_tag.get('src')

        if img_url:
            # Download and save the image
            response = requests.get(img_url)
            with open(os.path.join(folder, os.path.basename(img_url)), 'wb') as f:
                f.write(response.content)
        
        print(f"Downloaded image {i} of {len(img_tags)}")

        i += 1

def process_sitemap(sitemap_url, folder):
    print(f"Processing sitemap {sitemap_url}...")

    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.text, features="xml")  # Use 'xml.parser' for XML content

    # Find all URLs in the sitemap
    url_tags = soup.find_all('url')

    print(f"Found {len(url_tags)} URLs")

    for url_tag in url_tags:
        # Get the loc (URL) tag
        loc_tag = url_tag.find('loc')

        if loc_tag:
            # Extract the URL
            page_url = loc_tag.text.strip()

            print(f"Processing image urls from {page_url}...")
            # Download images from the page
            download_images(page_url, folder)

def main():
    # Replace 'your_sitemap_url_here' with the actual URL of the sitemap
    sitemap_url = input('Enter the sitemap URL:\n')
    image_folder = '../downloaded_images'

    os.makedirs(image_folder, exist_ok=True)
    
    # Download images from the pages listed in the sitemap
    process_sitemap(sitemap_url, image_folder)

if __name__ == "__main__":
    print("Starting...")
    main()
    print("Done!")
