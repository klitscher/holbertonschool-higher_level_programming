#!/usr/bin/python3
"""Module for class that inherits from a list"""


class MyList(list):
    """Class that inherits from a list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
