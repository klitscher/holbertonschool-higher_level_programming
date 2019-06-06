#!/usr/bin/python3
"""Module to write to a file"""


def write_file(filename="", text=""):
    """Function to write to a file"""

    with open(filename, encoding="utf-8", mode='w') as myFile:
        myFile.write(text)
    return(len(text))
