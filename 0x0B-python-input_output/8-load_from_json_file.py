#!/usr/bin/python3
"""Module to create an object form a json file"""


import json


def load_from_json_file(filename):
    """Function to create an object form a json file"""

    with open(filename, encoding="utf-8") as myFile:
        return json.load(myFile)
