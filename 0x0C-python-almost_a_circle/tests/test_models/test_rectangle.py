#!/usr/bin/python3
"""Testing module for rectangle class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Tests for Rectangle class"""


    #----------------Tests general------------
    def test_Int(self):
        """Test with int"""
        r1 = Rectangle(5, 899)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 899)

    def test_isSubclass(self):
        """Test if rectangle is a subclass of square"""
        r1 = Rectangle(5, 100)
        self.assertTrue(issubclass(Rectangle, Base))

    #----------------Tests for number of arguments------------

    def test_0Arguments(self):
        """Test if there is 0 argument"""
        self.assertRaises(TypeError, Rectangle)

    def test_1Arguments(self):
        """Test if there is 1 argument"""
        self.assertRaises(TypeError, Rectangle, 1)

    def test_tooManyArguments(self):
        """Test if there are too many arguments"""
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6)

    #----------------Tests for id inheritance---------------------

    def test_idNoArgs(self):
        """Test that id works with no arguments"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(5, 7)
        self.assertEqual(r1.id, r2.id - 1)

    def test_id(self):
        """Test that id works with argument"""
        r1 = Rectangle(4, 6, id='Hello')
        self.assertEqual(r1.id, 'Hello')

    #----------------Tests for width----------------------------
    def test_widthStr(self):
        """Test width with str"""
        self.assertRaises(TypeError, Rectangle, 'Hello', 1)

    def test_widthFloat(self):
        """Test width with float"""
        self.assertRaises(TypeError, Rectangle, 4.7, 1)

    def test_widthList(self):
        """Test width with list"""
        self.assertRaises(TypeError, Rectangle, [9, 8, 9], 1)

    def test_widthTuple(self):
        """Test width with tuple"""
        self.assertRaises(TypeError, Rectangle, (1, ), 1)

    def test_widthDict(self):
        """Test width with dicts"""
        self.assertRaises(TypeError, Rectangle,{"key": 1, "Key2": 'value'}, 1)

    def test_widthZero(self):
        """Test width == 0"""
        self.assertRaises(ValueError, Rectangle, 0, 6)

    def test_widthLessThanZeo(self):
        """Test width < 0"""
        self.assertRaises(ValueError, Rectangle, -9, 6)

    #----------------Tests for height--------------------------

    def test_heightStr(self):
        """Test height with str"""
        self.assertRaises(TypeError, Rectangle, 1, 'Hello')

    def test_heightFloat(self):
        """Test height with float"""
        self.assertRaises(TypeError, Rectangle, 1, 4.7)

    def test_heightList(self):
        """Test height with list"""
        self.assertRaises(TypeError, Rectangle, 1, [9, 8, 9])

    def test_heightTuple(self):
        """Test height with tuple"""
        self.assertRaises(TypeError, Rectangle, 1, (1, ))

    def test_heightDict(self):
        """Test height with dicts"""
        self.assertRaises(TypeError, Rectangle, 1, {"key": 1, "Key2": 'value'})

    def test_heightZero(self):
        """Test height == 0"""
        self.assertRaises(ValueError, Rectangle, 4, 0)

    def test_heightLessThanZeo(self):
        """Test height < 0"""
        self.assertRaises(ValueError, Rectangle, 9, -99)

    #----------------Tests for x-------------------------------

    def test_xStr(self):
        """Test x with str"""
        self.assertRaises(TypeError, Rectangle, 1, 5, 'Hello')

    def test_xFloat(self):
        """Test x with float"""
        self.assertRaises(TypeError, Rectangle, 1, 5, 4.7)

    def test_xList(self):
        """Test x with list"""
        self.assertRaises(TypeError, Rectangle, 1, 5, [9, 8, 9])

    def test_xTuple(self):
        """Test x with tuple"""
        self.assertRaises(TypeError, Rectangle, 1, 5, (1, ))

    def test_xDict(self):
        """Test x with dicts"""
        self.assertRaises(TypeError, Rectangle, 1, 5, {"key": 1})

    def test_xLessThanZeo(self):
        """Test x < 0"""
        self.assertRaises(ValueError, Rectangle, 9, 99, -9, 8)

    #----------------Tests for y----------------------------------

    def test_yStr(self):
        """Test y with str"""
        self.assertRaises(TypeError, Rectangle, 1, 5, 8, 'Hello')

    def test_yFloat(self):
        """Test y with float"""
        self.assertRaises(TypeError, Rectangle, 1, 5, 8, 4.7)

    def test_yList(self):
        """Test y with list"""
        self.assertRaises(TypeError, Rectangle, 1, 5, 8, [9, 8, 9])

    def test_yTuple(self):
        """Test y with tuple"""
        self.assertRaises(TypeError, Rectangle, 1, 6, 8, (1, ))

    def test_yDict(self):
        """Test y with dicts"""
        self.assertRaises(TypeError, Rectangle, 1, 7, 8, {"key": 1})

    def test_yLessThanZeo(self):
        """Test y < 0"""
        self.assertRaises(ValueError, Rectangle, 9, 99, 9, -8)

    #----------------Tests for area method-------------------------------

    def test_areaCorrect(self):
        """Test that area works"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 20)

    def test_areaArguments(self):
        """Test that area accepts no arguments"""
        r1 = Rectangle(9, 100)
        self.assertRaises(TypeError, r1.area, 6)

    #----------------Tests for display method-------------------------------

    def test_displayArgument(self):
        """Test that display takes no arguments"""
        r1 = Rectangle(2, 3)
        self.assertRaises(TypeError, r1.display, 1)
