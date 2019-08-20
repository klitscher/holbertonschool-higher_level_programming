#!/usr/bin/python3
"""Module to find the peak in a list of numbers"""


def find_peak(list_of_integers):
    """Function to find peak"""

    if len(list_of_integers) < 1:
        return ("None")
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    base = list_of_integers[0]
    for i in range(1, len(list_of_integers)):
        if base > list_of_integers[i]:
            return (base)
        if base < list_of_integers[i]:
            base = list_of_integers[i]
    return (base)
