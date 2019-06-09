#!/usr/bin/python3
"""Module for creating a base class"""


class Base:
    """Basic class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
