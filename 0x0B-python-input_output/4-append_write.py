#!/usr/bin/python3
"""Module to append text to a file"""


def append_write(filename="", text=""):
    """Function to append text to a file"""

    with open(filename, encoding="utf-8", mode="a") as myFile:
        myFile.write(text)
    return len(text)
