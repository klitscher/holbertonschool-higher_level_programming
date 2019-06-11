#!/usr/bin/python3
"""Module for square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overload method"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id,
                                             self.x, self.y, self.size)

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square attributes"""
        i = 0
        if len(args) > 0:
            for arg in args:
                i += 1
                if i == 1:
                    self.id = arg
                if i == 2:
                    self.size = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            if kwargs is not None:
                li = ["id", "size", "x", "y"]
                for key, value in kwargs.items():
                    if key in li:
                        setattr(self, key, value)
