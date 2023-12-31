import os
import requests
from bs4 import BeautifulSoup


def download_images(base, url, folder):
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
        print(f"Image URL: {img_url}")
        full_img_url = f"{base}{img_url}"

        if img_url.startswith('http') or img_url.startswith('https'):
            full_img_url = img_url

        if full_img_url:
            # Download and save the image
            response = requests.get(full_img_url)
            with open(os.path.join(folder, os.path.basename(full_img_url)), 'wb') as f:
                f.write(response.content)
        
        print(f"Downloaded image {i} of {len(img_tags)}")

        i += 1

def process_sitemap(base_url, sitemap_url, folder):
    print(f"Processing sitemap {base_url + '/' + sitemap_url}...")
    sitemap = f"{base_url}/{sitemap_url}"
    response = requests.get(sitemap)
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
            download_images(base_url, page_url, folder)

def main():
    # Replace 'your_sitemap_url_here' with the actual URL of the sitemap
    base_url = input('Enter the base URL:\n')
    sitemap_url = input('Enter the sitemap URL:\n')
    image_folder = './downloaded_images'

    os.makedirs(image_folder, exist_ok=True)
    
    # Download images from the pages listed in the sitemap
    process_sitemap(base_url, sitemap_url, image_folder)

if __name__ == "__main__":
    print("Starting...")
    main()
    print("Done!")
