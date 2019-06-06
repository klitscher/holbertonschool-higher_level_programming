#!/usr/bin/python3
"""Module to get dictionary description"""


def class_to_json(obj):
    """Function to get dictionary description"""

    li = obj.__dict__
    dic = {}
    for key, value in li.items():
        if isinstance(value, list) or isinstance(value, dict) or isinstance(
                value, str) or isinstance(value, int) or isinstance(
                    value, bool):
            dic.update({key: value})
    return dic
