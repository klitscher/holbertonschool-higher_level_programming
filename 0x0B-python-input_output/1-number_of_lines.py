#!/usr/bin/python3
"""Module to return number of lines"""


def number_of_lines(filename=""):
    """Function to return the number of lines"""

    with open(filename, encoding="utf-8") as myFile:
        lineNum = 0
        while True:
            line = myFile.readline()
            if not line:
                break
            lineNum += 1
    return lineNum
