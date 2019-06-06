#!/usr/bin/python3
"""Module to return a python object from JSON"""

import json


def from_json_string(my_str):
    """Function to return a python object from JSON"""

    return json.loads(my_str)
