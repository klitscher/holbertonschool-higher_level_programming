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

    #----------------Tests update args-----------------------------

    def test_update1Args(self):
        """Test correct output"""
        s1 = Square(10, 10, 10)
        s1.update(89)
        self.assertEqual(s1.id, 89)

    def test_update2Args(self):
        """Test two args"""
        s1 = Square(10, 10, 10)
        s1.update(89, 72)
        li = [s1.id, s1.width]
        self.assertListEqual(li, [89, 72])

    def test_update3Args(self):
        """Test three args"""
        s1 = Square(10, 10, 10)
        s1.update(89, 72, 9)
        li = [s1.id, s1.size, s1.x]
        self.assertListEqual(li, [89, 72, 9])

    def test_update4Args(self):
        """Test four args"""
        s1 = Square(10, 10, 10)
        s1.update(89, 72, 9, 44)
        li = [s1.id, s1.size, s1.x, s1.y]
        self.assertListEqual(li, [89, 72, 9, 44])

    def test_update5Args(self):
        """Test five args"""
        s1 = Square(10, 10, 10)
        s1.update(89, 72, 9, 64, 7)
        li = [s1.id, s1.size, s1.x, s1.y]
        self.assertListEqual(li, [89, 72, 9, 64])

    def test_updateEmpty(self):
        """Test no argument to update"""
        s1 = Square(4)
        s1.update()
        li = [s1.id, s1.size, s1.x, s1.y]
        self.assertListEqual(li, [s1.id, 4, 0, 0])

    def test_updateStr(self):
        """Test with string in each spot but id"""
        s1 = Square(4)
        good = [s1.id, 1, 2, 3]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = 'Hello'
            self.assertRaises(TypeError, s1.update, *bad)

    def test_updateFloat(self):
        """Test with float in each spot but id"""
        s1 = Square(4)
        good = [s1.id, 1, 2, 3]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = 3.8
            self.assertRaises(TypeError, s1.update, *bad)

    def test_updateList(self):
        """Test with list in each spot but id"""
        s1 = Square(4)
        good = [s1.id, 1, 2, 3]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = [3, 5, 8]
            self.assertRaises(TypeError, s1.update, *bad)

    def test_updateList(self):
        """Test with tuple in each spot but id"""
        s1 = Square(4)
        good = [s1.id, 1, 2, 3]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = (3, 5, 8)
            self.assertRaises(TypeError, s1.update, *bad)

    def test_updateList(self):
        """Test with dict in each spot but id"""
        s1 = Square(4)
        good = [s1.id, 1, 2, 3]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = {"Key": 1, "Key2": 'Hello'}
            self.assertRaises(TypeError, s1.update, *bad)

    def test_updateNegatives(self):
        """Test with negatives in each spot but id"""
        s1 = Square(4)
        good = [s1.id, 1, 2, 3]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = -8
            self.assertRaises(ValueError, s1.update, *bad)

    def test_update0(self):
        """Test square with zero"""
        s1 = Square(4)
        good = [s1.id, 1, 2, 3]
        for i in range(1, 2):
            bad = good.copy()
            bad[i] = 0
            self.assertRaises(ValueError, s1.update, *bad)

    #----------------Tests for update method: kwargs--------------------------

    def test_updateKwargWithArgs(self):
        """Test kwargs with args"""
        s1 = Square(4)
        s1.update(4, x=88)
        li = [s1.id, s1.size, s1.x, s1.y]
        self.assertListEqual(li, [4, 4, 0, 0])

    def test_updateKwargsNotAttr(self):
        """Test arg not an attribute"""
        s1 = Square(4)
        s1.update(bad=88)
        li = [s1.id, s1.size, s1.x, s1.y]
        self.assertListEqual(li, [s1.id, 4, 0, 0])

    def test_updateKwargString(self):
        """Test kwarg with strings"""
        s1 = Square(4)
        self.assertRaises(TypeError, s1.update, size='Hello')
        self.assertRaises(TypeError, s1.update, x='Hello')
        self.assertRaises(TypeError, s1.update, y='Hello')

    def test_updateKwargFloat(self):
        """Test kwarg with floats"""
        s1 = Square(4)
        self.assertRaises(TypeError, s1.update, size=3.4)
        self.assertRaises(TypeError, s1.update, x=3.4)
        self.assertRaises(TypeError, s1.update, y=3.4)

    def test_updateKwargList(self):
        """Test kwarg with lists"""
        s1 = Square(4)
        self.assertRaises(TypeError, s1.update, size=[1, 2 , 3])
        self.assertRaises(TypeError, s1.update, x=[1, 2 , 3])
        self.assertRaises(TypeError, s1.update, y=[1, 2 , 3])

    def test_updateKwargTuples(self):
        """Test kwarg with tuples"""
        s1 = Square(4)
        self.assertRaises(TypeError, s1.update, size=(1, ))
        self.assertRaises(TypeError, s1.update, x=(1, ))
        self.assertRaises(TypeError, s1.update, y=(1, ))

    def test_updateKwargDict(self):
        """Test kwarg with Dicts"""
        s1 = Square(4)
        self.assertRaises(TypeError, s1.update, size={"Key": 1, "Key2": 'hello'})
        self.assertRaises(TypeError, s1.update, x={"Key": 1, "Key2": 'hello'})
        self.assertRaises(TypeError, s1.update, y={"Key": 1, "Key2": 'hello'})

    def test_updateKwarg0(self):
        """Test kwarg with 0"""
        s1 = Square(4)
        self.assertRaises(ValueError, s1.update, size=0)

    def test_updateKwargTuples(self):
        """Test kwarg with negatives"""
        s1 = Square(4)
        self.assertRaises(ValueError, s1.update, size=-8)
        self.assertRaises(ValueError, s1.update, x=-8)
        self.assertRaises(ValueError, s1.update, y=-8)

    #----------------Tests for to_dictionary method-------------------------

    def test_toDictCorrect(self):
        """Test correct output"""
        s1 = Square(2, 1, 9)
        l1 = [s1.id, s1.size, s1.x, s1.y]
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1)
        s2.update(**s1_dictionary)
        l2 = [s2.id, s2.size, s2.x, s2.y]
        self.assertListEqual(l1, l2)

    def test_toDictArguments(self):
        s1 = Square(3)
        self.assertRaises(TypeError, s1.to_dictionary, 1)
