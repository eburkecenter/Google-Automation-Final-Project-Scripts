#!/usr/bin/env python3
from datetime import datetime
import os
import reports
import emails
# folder = "supplier-data/descriptions/"
folder = "C:/Users/eburk/Desktop/text-files"


def process_data(folder):
    """ Function returns a list of summary in the form name \n description"""
    # saving input folder into a variable
    input_folder = os.listdir(folder)
    summary = str()
    # reading each line in the python file
    for file in input_folder:
        file_path = os.path.join(folder, file)
        f, x = os.path.splitext(file)
        with open(file_path, 'r') as files:
            lines = files.readlines()
            summary += "name: "+lines[0]+"weight: "+lines[1]+"<br/>" + "\n"

    return summary


def main():

    summary = process_data(folder)
    print(summary)
    reports.generate_report(
        "/tmp/processed.pdf", datetime.now().strftime("%m/%d/%Y %H:%M"), summary)


if __name__ == "__main__":
    main()
    sender = "automation@example.com"  # from
    receiver = "<>@example.com"  # to
    subject = "Upload Completed - Online Fruit Store"
    body = " All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate(
        sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)
