#! /usr/bin/env python3

import requests
import re
import os
from pathlib import Path

url = "http://localhost/upload/"
home = str(Path.home())
new_images_dir = "/supplier-data/images"
os.chdir(home + new_images_dir)
cwd = os.getcwd()

def image_uploader():
    images = os.listdir(cwd)
    for image in images:
        regex = r"(jpeg)"
        image_search = re.search(regex, image)
        if image_search == None:
            continue
        image_search = image_search.groups()
        if image_search[0] == "jpeg":
            url = "http://localhost/upload/"
            with open(home + new_images_dir + image, "rb") as opened:
                r = requests.post(url, files = {"file": opened})

image_uploader()
