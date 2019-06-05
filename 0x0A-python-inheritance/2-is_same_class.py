#!/usr/bin/python3
"""Module to return if object is exactly an instance"""


def is_same_class(obj, a_class):
    """Function to check object"""
    if type(obj) is a_class:
        return True
    else:
        return False
