#! /usr/bin/env python3

import os
import re
from PIL import Image
from pathlib import Path

home = str(Path.home())
new_images_dir = "/supplier-data/images"
os.chdir(home + new_images_dir)
cwd = os.getcwd()

def image_corrector():
    images = os.listdir(cwd)
    for image in images:
        im = Image.open(image)
        regex - r"(\d+)"
        image_search = re.search(regex, image)
        image_search.groups()
        im.resize((600, 400)).convert("RGB").save(image_search[0] + ".jpeg")

image_corrector()
