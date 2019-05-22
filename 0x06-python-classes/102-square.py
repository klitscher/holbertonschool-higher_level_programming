#!/usr/bin/python3
class Square:
    """Class to define a square."""
    def __init__(self, size=0):
        """Initialize class with size.
        Check to see if the size entered is not an integer
        Args:
        size (int): size of the square.
        """
        self.__size = size

    def area(self):
        """Return the area of a square"""
        return self.__size * self.__size

    @property
    def size(self):
        """int: Returns the size of the square.
        Checks for errors, otherwise assigne value to the field__size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
