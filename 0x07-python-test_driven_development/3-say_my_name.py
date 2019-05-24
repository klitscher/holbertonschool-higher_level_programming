#!/usr/bin/python3
"""Module to print a first name and or a last name"""


def say_my_name(first_name, last_name=""):
    """Function to print first and or last name"""

    # Checks if the entered name is a string or not
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
