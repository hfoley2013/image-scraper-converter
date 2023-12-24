# Web Scraper and Image Converter

This repo contains four scripts for use as required. The file should be used in the following order:

1. `scrape.py`
2. `converter.py`
3. `move_files.py`
4. `delete_all_images.py`

## scrape.py

This script takes in a url for a sitemap and then uses `beautifulsoup4` and the `requests` library to visit each `<url>` extracted from the sitemap and retrieve all images.

## converter.py

This script converts all images downloaded by `scrape.py` from `png` to `webp` format.

## move_files.py

This script moves the `webp` formatted images into a desired destination folder. The existing destination folder is `converted_images`. You can rename this location as desired.

## delete_all_images.py

This script deletes all images in the downloaded_images and converted_images folders to reset for the next url.