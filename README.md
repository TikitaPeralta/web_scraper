# Scraping WikiHow - Images & Captions
## Description
This repository contains a gitignore, a JSON file, a python file and the images scraped from WikiHow. The purpose of this project was to scrape the site: [WikiHow.com](https://www.wikihow.com/Main-Page) for all images and their captions. This project was done in python. In the later YouTube video I talked through my process and went through the result.

## Installation
### Setting up the virtual environment
pip install virtualenv
python3 -m venv venv
source venv/bin/activate

### Create gitignore
touch .gitignore (no output expected)
open .gitignore and write in venv

### Installing dependencies
pip install requests
pip install beautifulsoup4
pip install pathlib
pip install urllib3
pip install pillow


## Usage
### Import modules
```
import requests
import urllib.request
from pathlib import Path
import pathlib
import os
from bs4 import BeautifulSoup
from random import randint 
from time import sleep
import json
from PIL import Image
```
- access every image independent of page, i.e. the main page's layout is different to every article page
- exclude png/svg from img finding, as the majority of these were icons or profile photos from comments
- if link is found, add to list of URLs
- iterate through list of URLs until finished, while len(list) > 0
- no repetitions = add to 'URL_seen' list and check if not in
- follow link for each image and download to documents/webscrape/photos file
- place into JSON format

### JSON format
```
{
    "1" : ["caption", "img link", "path to img"]
}
```

## YouTube Video
[Scraping Project Video](https://youtu.be/--vqOqxfRDU?si=F4_1Z0_ewmMnG1fr)


