# web_scraper

file on desktop: images for each img to be stored
JSON file: img src, img current path, img alt

format:

{
    "1" : ["img src", "img current path", "img alt"]
}

- access every image independent of page
- exclude png/svg from img finding
- if link is found, add to list of URLs
- iterate through list of URLs until finished
- follow link for each image and download to documents/webscrape/photos file
- in JSON: res['src'], documents/webscrape/name-of-file.jpeg, res['alt']