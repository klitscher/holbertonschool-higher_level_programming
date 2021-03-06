#!/usr/bin/python3
"""Module to define a rectangle"""


class Rectangle:
    """Class for the rectangle
    Attributes:
        number_of_instances: number of instances of class
        print_symbol: symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """method to find area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """method to find the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """method to dertermine which rectangle is bigger"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new instance of a rectangle"""
        new = cls()
        new.width = size
        new.height = size
        return new

    def __str__(self):
        """Visual representation of square"""
        li = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            li.append(str(self.print_symbol) * self.__width)
        return '\n'.join(li)

    def __repr__(self):
        """String rep of the rectangle"""
        return "{}({}, {})".format((type(self).__name__),
                                   self.__width, self.__height)

    def __del__(self):
        """Add messege when instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __init__(self, width=0, height=0):
        """initilization for rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
