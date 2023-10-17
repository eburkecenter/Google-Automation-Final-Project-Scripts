#!/usr/bin/env python3
""" Welcome to Week 4 of Google Automation Final Project written in Python 

                            Catalog Information Processing 
"""
# importing library
from PIL import Image
import os
import sys

# Defining the input path for image files
input_path = "supplier-data/images"

image_folder = os.listdir(input_path)
# Defining the output path for images that have been processed
output_path = "supplier-data/images"


# Defining the criteria for processing images
# Pixel Size of the images and format for the images
img_size = (600, 400)
img_format = ".jpeg"


def process_image(image, folder, size, output):
    """ 
     Creating a function that does the following: 
    # 1. converts images to standard RBG
    # 2. Rotate the image 90° clockwise
    # 3. Resize the image from 192x192 to 128x128
    # 4. Save the image to a new folder in .jpeg format

    """
    new_image_name, x = os.path.splitext(image)
    img_path = os.path.join(folder, image)
    im = Image.open(img_path)
    new_image = im.convert("RGB").resize(size)
    new_image.save(output + "/" + new_image_name + img_format)


def main():
    """Main function that is used to iterate through the image folder
       The function skips over hidden files then calls process_image function
       The function also catch errors that may occur when tring to process a function"""
    for image in image_folder:
        if image.startswith("."):
            continue
        else:
            try:
                process_image(image, input_path, img_size, output_path)
            except OSError as error:
                print(error)
                pass


# Running program
if __name__ == "__main__":
    main()
