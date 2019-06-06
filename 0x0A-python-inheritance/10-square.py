#!/usr/bin/python3
"""Module to inherit from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that creates a square"""

    def __init__(self, size):
        """Instantiation"""
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)
