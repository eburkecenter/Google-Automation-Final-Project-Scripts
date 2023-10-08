#!/usr/bin/env python3
""" Welcome to Week 1 of Google Automation Final Project written in Python 

                            Manipulating Images 
"""

# importing library
from PIL import Image
import os
import sys

# Reading images from location

# print(len(sys.argv))
if len(sys.argv) <= 2:
    print("Please enter arguments input path and output path")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]
# print(output_path)
angle = 270
size = (128, 128)
# reading images
image_folder = os.listdir(input_path)


def process_image(image, folder, angle, size, output):
    """ 
     Creating a function that does the following: 
    # 1. converts images to standard RBG
    # 2. Rotate the image 90° clockwise
    # 3. Resize the image from 192x192 to 128x128
    # 4. Save the image to a new folder in .jpeg format

    """
    img_path = os.path.join(folder, image)
    im = Image.open(img_path)
    new_image = im.convert("RGB").rotate(angle).resize(size)
    # print(new_image)
    new_image.save(output+"/"+image, "JPEG")


def main():
    """Main function that is used to iterate through the image folder
       The function skips over hidden files then calls process_image function
       The function also catch errors that may occur when tring to process a function"""
    for image in image_folder:
        if image.startswith("."):
            continue
        else:
            # image=image.split(".")
            try:
                process_image(image, input_path, angle, size, output_path)
            except OSError as error:
                print(error)
                pass


# Running program
if __name__ == "__main__":
    main()
