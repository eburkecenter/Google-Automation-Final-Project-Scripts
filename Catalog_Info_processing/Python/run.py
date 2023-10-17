#! /usr/bin/env python3
# importing libraries
import os
import sys
import requests
import json

#

# saving input folder into a variable
folder = "supplier-data/descriptions/"
input_folder = os.listdir(folder)

# reading each line in the python file
for file in input_folder:
    file_path = os.path.join(folder, file)
    f, x = os.path.splitext(file)
    with open(file_path, 'r') as files:
        lines = files.readlines()
        weight = lines[1][:-5]
        output_dict = {}
        output_dict["name"] = lines[0]
        output_dict["weight"] = int(weight)
        output_dict["description"] = lines[2]
        output_dict["image_name"] = f+".jpeg"
        print(output_dict)
        # replace <corpweb-external-IP>with given ip address
        requests.post("http://[linux-instance-external-IP]/fruits/",
                      data=output_dict)
