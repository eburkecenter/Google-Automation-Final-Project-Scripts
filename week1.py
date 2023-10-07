#!/usr/bin/env python3
""" Welcome to Week 1 of Google Automation Final Project written in Python 

                            Manipulating Images 
"""
# importing library
from PIL import Image
import os
from multiprocessing import Pool
# Reading images from location
# images = input("Please enter path to location of images: ")

# Hard path for testing purposes
# path = "C:/Users/eburk/Desktop/Screenshots2"
input_path = "C:/Users/eburk/Desktop/pics"
output_path = "C:/Users/eburk/Desktop/pics2"
angle = 90
size = (128, 128)
# reading images
image_folder = os.listdir(input_path)

# Creating a Pool for multi threading.

""" 
     Creating a function that does the following: 
# 1. Rotate the image 90° clockwise
# 2. Resize the image from 192x192 to 128x128
# 3. Save the image to a new folder in .jpeg format

"""


def process_image(image, folder, angle, size, output):
    im = Image.open(folder+"/" + image)
    new_image = im.rotate(angle).resize(size)
    new_path = os.path.join(output, image)
    new_image.save(new_path, "jpeg")


# Running program
if __name__ == "__main__":
    for image in image_folder:
        if image.endswith('.ini'):
            continue
        try:
            process_image(image, input_path, angle, size, output_path)
        except OSError as error:
            print(error)
            pass
