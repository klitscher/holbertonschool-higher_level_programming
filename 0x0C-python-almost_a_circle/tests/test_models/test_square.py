#!/usr/bin/python3
"""Testing module for base class"""


import unittest
#import io
#import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquareClass(unittest.TestCase):
    """Tests for Square class"""


    #----------------Tests general----------------------------

    def test_squareSub(self):
        """Tests if square is a subclass of Rectangle"""
        s1 = Square(3)
        self.assertTrue(issubclass(Square, Rectangle))

    def test_squareInstance(self):
        """Tests if square is an instance of Base"""
        s1 = Square(2)
        self.assertTrue(isinstance(s1, Base))

    #----------------Tests number of arguments------------------

    def test_square(self):
        """Test empty square"""
        self.assertRaises(TypeError, Square)

    def test_squareTooManyArgs(self):
        """Test too many arguments in square"""
        self.assertRaises(TypeError, Square, 1, 2, 3, 4, 5, 6)

  #----------------Tests arguments-----------------------------

    def test_squareZero(self):
        """Test size with zero"""
        self.assertRaises(ValueError, Square, 0)

    def test_squareNegative(self):
        """Test size with negatives"""
        self.assertRaises(ValueError, Square, -1)

    def test_sizeStr(self):
        """Test size with str"""
        self.assertRaises(TypeError, Square, 'Hello')

    def test_sizeFloat(self):
        """Test size with float"""
        self.assertRaises(TypeError, Square, 4.7)

    def test_sizeList(self):
        """Test size with list"""
        self.assertRaises(TypeError, Square, [9, 8, 9])

    def test_sizeTuple(self):
        """Test size with tuple"""
        self.assertRaises(TypeError, Square, (1, ))

    def test_sizeDict(self):
        """Test size with dicts"""
        self.assertRaises(TypeError, Square,{"key": 1, "Key2": 'value'})
