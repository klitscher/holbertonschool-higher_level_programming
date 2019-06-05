#!/usr/bin/python3
"""Module to add an attribute if possible"""


def add_attribute(obj, att, value):
    """Adds an attribute if possible"""

    li = dir(obj)

    for i in li:
        if i == '__slots__':
            for j in li:
                if j == att:
                    setattr(obj, att, value)
                    return
            raise TypeError("can't add new attribute")

    for k in li:
        if k == '__dict__':
            setattr(obj, att, value)
            return
    raise TypeError("can't add new attribute")
