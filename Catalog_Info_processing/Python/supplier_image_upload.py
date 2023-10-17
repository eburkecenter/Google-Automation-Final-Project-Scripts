#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
path_to_image_files = "supplier-data/images"
full_path = os.listdir(path_to_image_files)
for image in full_path:
    if image.lower().endswith(".jpeg"):
        with open(os.path.join(path_to_image_files, image), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
