#!/usr/bin/python3
"""Module to print text differntly"""


def text_indentation(text):
    """Function to print the text"""

    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    count = 0
    new = ""
    for i in range(len(text)):
        if text[i] == ".":
            new = text[count:(i + 1)]
            print("{}\n".format(new.lstrip()))
            count = i + 1
        elif text[i] == "?":
            new = text[count:(i + 1)]
            print("{}\n".format(new.lstrip()))
            count = i + 1
        elif text[i] == ":":
            new = text[count:(i + 1)]
            print("{}\n".format(new.lstrip()))
            count = i + 1
        elif i + 1 == len(text):
            new = text[count:(i + 1)]
            print("{}".format(new.lstrip()), end="")
