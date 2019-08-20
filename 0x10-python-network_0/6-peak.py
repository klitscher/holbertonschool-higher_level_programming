#!/usr/bin/python3
"""Module to find the peak in a list of numbers"""


def find_peak(list_of_integers):
    """Driver Function for peak"""
    length = len(list_of_integers)
    if length < 1:
        return ("None")
    result = get_peak(list_of_integers, 0, length - 1, length)
    return (result)

def get_peak(int_list, low, high, n):
    """Work function for peak"""
    mid = int(low + (high - low)/2)

    if ((mid == 0 or int_list[mid - 1] <= int_list[mid]) and (
            mid == n - 1 or int_list[mid + 1] <= int_list[mid])):
        return (int_list[mid])

    elif (mid > 0 and int_list[mid - 1] > int_list[mid]):
        return get_peak(int_list, low, (mid - 1), n)

    else:
        return get_peak(int_list, (mid + 1), high, n)
