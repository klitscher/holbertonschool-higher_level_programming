#!/usr/bin/python3
"""Checks the inheritence of an object"""

def is_kind_of_class(obj, a_class):
    """Checks the inheritence of an object"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
