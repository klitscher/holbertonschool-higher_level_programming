#!/usr/bin/python3
"""Module to read a text file"""


def read_file(filename=""):
    """Function to read a file"""

    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
