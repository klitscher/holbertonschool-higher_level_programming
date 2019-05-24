#!/usr/bin/python3
"""Module to print a square with #"""


def print_square(size):
    """Function to print the square"""
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    # Check if size is less than 0
    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        print("#" * size)
