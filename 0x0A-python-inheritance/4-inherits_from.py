#!/usr/bin/python3
"""Checks if is subclass"""


def inherits_from(obj, a_class):
    """Checks if is subclass"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
