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
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Return the area of a square"""
        return self.__size * self.__size
