#!/usr/bin/python3
"""Module to write an object ot a text file using JSON"""


import json


def save_to_json_file(my_obj, filename):
    """Function to write an object ot a text file using JSON"""

    with open(filename, encoding="utf-8", mode='w') as myFile:
        myFile.write(json.dumps(my_obj))
