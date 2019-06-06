#!/usr/bin/python3
"""Module to inherit from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inheits from base Geometry"""

    def __init__(self, width, height):
        """Instantiates the class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
