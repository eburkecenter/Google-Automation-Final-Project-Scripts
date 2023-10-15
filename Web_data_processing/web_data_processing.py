#!/usr/bin/env python3
""" Welcome to Week 2 of Google Automation Final Project written in Python 

                    Processing Text Files to Run on Web Service 
"""
# importing libraries
import os
import sys
import requests
import json

# Reading files from directory and entering them into a list
# checking to ensure folder containing files is passed as an argument
if len(sys.argv) <= 1:
    print("Please enter the folder containing files as a argument")
    sys.exit(1)

# saving input folder into a variable
folder = sys.argv[1]
input_folder = os.listdir(folder)

# reading each line in the python file
for file in input_folder:
    file_path = os.path.join(folder, file)
    with open(file_path, 'r') as file:
        lines = file.readlines().strip()
        output_dict = {}
        output_dict["title"] = lines[0]
        output_dict["name"] = lines[1]
        output_dict["date"] = lines[2]
        output_dict["feedback"] = lines[3]
        # replace <corpweb-external-IP>with given ip address
        requests.post("http://<corpweb-external-IP>/feedback/",
                      data=output_dict)


# Written to test parsing locally
""" out_file = open("reviews.json", "w")
json.dump(output_list, out_file, sort_keys=False)
out_file.close() """
