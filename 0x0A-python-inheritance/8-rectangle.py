#!/usr/bin/python3
"""Module to inherit from BaseGeometry"""


class BaseGeometry:
    """Base Class"""

    def area(self):
        """Get area of the geometry"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Class that inheits from base Geometry"""

    def __init__(self, width, height):
        """Instantiates the class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
