#!/usr/bin/python3
"""Module to create a BaseGeometry class"""


class BaseGeometry:
    """Base Class"""
    def area(self):
        """Get area of the geometry"""
        raise Exception('area() is not implemented')
