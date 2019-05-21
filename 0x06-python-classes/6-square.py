#!/usr/bin/python3
class Square:
    """Class to define a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize class with size.
        Check to see if the size entered is not an integer
        Args:
        size (int): size of the square.
        position: Coordinate of the square
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """Prints a visual representation of the square"""
        count = self.__position[0]
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for row in range(0, self.__size):
                if count > 0:
                       for i in range(0, count):
                           print("_".format(), end="")
                for col in range(0, self.__size):
                   print("#".format(), end="")
                print()
    @property
    def position(self):
        """int: position of the square in tuple format.

        Checks if there are any bad values.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not all(isinstance(n, int) for n in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
