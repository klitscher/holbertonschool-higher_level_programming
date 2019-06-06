#!/usr/bin/python3
"""Module to read number of lines"""


def read_lines(filename="", nb_lines=0):
    """Function to read number of lines"""

    with open(filename, encoding="utf-8") as myFile:
        if nb_lines <= 0:
            print(myFile.read(), end="")
            return
        for i in range(nb_lines):
            print(myFile.readline(), end="")
