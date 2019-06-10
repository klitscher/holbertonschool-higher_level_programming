#!/usr/bin/python3
"""Testing module for rectangle class"""


import unittest
#import io
#import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Tests for Rectangle class"""


    #----------------Tests general----------------------------

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
        """
    def test_displayCorrect(self):
        Test that checks it printed correctly
        r1 = Rectangle(2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        self.assertEqual(s, "##\n##\n")
        """
    #----------------Tests for __str__ method-------------------------------

    # Not sure how this would fail/test for it

    #----------------Tests for update method: args--------------------------

    def test_update1Args(self):
        """Test correct output"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

    def test_update2Args(self):
        """Test two args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 72)
        li = [r1.id, r1.width]
        self.assertListEqual(li, [89, 72])

    def test_update3Args(self):
        """Test three args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 72, 9)
        li = [r1.id, r1.width, r1.height]
        self.assertListEqual(li, [89, 72, 9])

    def test_update4Args(self):
        """Test four args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 72, 9, 44)
        li = [r1.id, r1.width, r1.height, r1.x]
        self.assertListEqual(li, [89, 72, 9, 44])

    def test_update5Args(self):
        """Test five args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 72, 9, 64, 7)
        li = [r1.id, r1.width, r1.height, r1.x, r1.y]
        self.assertListEqual(li, [89, 72, 9, 64, 7])

    def test_update6Args(self):
        """Test six args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 72, 9, 64, 7, 9)
        li = [r1.id, r1.width, r1.height, r1.x, r1.y]
        self.assertListEqual(li, [89, 72, 9, 64, 7])


    def test_updateEmpty(self):
        """Test no argument to update"""
        r1 = Rectangle(2, 4)
        r1.update()
        li = [r1.id, r1.width, r1.height, r1.x, r1.y]
        self.assertListEqual(li, [r1.id, 2, 4, 0, 0])

    def test_updateStr(self):
        """Test with string in each spot but id"""
        r1 = Rectangle(2, 4)
        good = [r1.id, 1, 2, 3, 4]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = 'Hello'
            self.assertRaises(TypeError, r1.update, *bad)

    def test_updateFloat(self):
        """Test with float in each spot but id"""
        r1 = Rectangle(2, 4)
        good = [r1.id, 1, 2, 3, 4]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = 3.8
            self.assertRaises(TypeError, r1.update, *bad)

    def test_updateList(self):
        """Test with list in each spot but id"""
        r1 = Rectangle(2, 4)
        good = [r1.id, 1, 2, 3, 4]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = [3, 5, 8]
            self.assertRaises(TypeError, r1.update, *bad)

    def test_updateList(self):
        """Test with tuple in each spot but id"""
        r1 = Rectangle(2, 4)
        good = [r1.id, 1, 2, 3, 4]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = (3, 5, 8)
            self.assertRaises(TypeError, r1.update, *bad)

    def test_updateList(self):
        """Test with dict in each spot but id"""
        r1 = Rectangle(2, 4)
        good = [r1.id, 1, 2, 3, 4]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = {"Key": 1, "Key2": 'Hello'}
            self.assertRaises(TypeError, r1.update, *bad)

    def test_updateNegatives(self):
        """Test with negatives in each spot but id"""
        r1 = Rectangle(2, 4)
        good = [r1.id, 1, 2, 3, 4]
        for i in range(1, len(good)):
            bad = good.copy()
            bad[i] = -8
            self.assertRaises(ValueError, r1.update, *bad)

    def test_update0(self):
        """Test width and height with zero"""
        r1 = Rectangle(2, 4)
        good = [r1.id, 1, 2, 3, 4]
        for i in range(1, 3):
            bad = good.copy()
            bad[i] = 0
            self.assertRaises(ValueError, r1.update, *bad)

    #----------------Tests for update method: kwargs--------------------------

    def test_updateKwargWithArgs(self):
        """Test kwargs with args"""
        r1 = Rectangle(3, 4)
        r1.update(4, x=88)
        li = [r1.id, r1.width, r1.height, r1.x, r1.y]
        self.assertListEqual(li, [4, 3, 4, 0, 0])

    def test_updateKwargsNotAttr(self):
        """Test arg not an attribute"""
        r1 = Rectangle(3, 4)
        r1.update(bad=88)
        li = [r1.id, r1.width, r1.height, r1.x, r1.y]
        self.assertListEqual(li, [r1.id, 3, 4, 0, 0])

    def test_updateKwargString(self):
        """Test kwarg with strings"""
        r1 = Rectangle(3, 4)
        self.assertRaises(TypeError, r1.update, width='Hello')
        self.assertRaises(TypeError, r1.update, height='Hello')
        self.assertRaises(TypeError, r1.update, x='Hello')
        self.assertRaises(TypeError, r1.update, y='Hello')

    def test_updateKwargFloat(self):
        """Test kwarg with floats"""
        r1 = Rectangle(3, 4)
        self.assertRaises(TypeError, r1.update, width=3.4)
        self.assertRaises(TypeError, r1.update, height=3.4)
        self.assertRaises(TypeError, r1.update, x=3.4)
        self.assertRaises(TypeError, r1.update, y=3.4)

    def test_updateKwargList(self):
        """Test kwarg with lists"""
        r1 = Rectangle(3, 4)
        self.assertRaises(TypeError, r1.update, width=[1, 2 , 3])
        self.assertRaises(TypeError, r1.update, height=[1, 2 , 3])
        self.assertRaises(TypeError, r1.update, x=[1, 2 , 3])
        self.assertRaises(TypeError, r1.update, y=[1, 2 , 3])

    def test_updateKwargTuples(self):
        """Test kwarg with tuples"""
        r1 = Rectangle(3, 4)
        self.assertRaises(TypeError, r1.update, width=(1, ))
        self.assertRaises(TypeError, r1.update, height=(1, ))
        self.assertRaises(TypeError, r1.update, x=(1, ))
        self.assertRaises(TypeError, r1.update, y=(1, ))

    def test_updateKwargDict(self):
        """Test kwarg with Dicts"""
        r1 = Rectangle(3, 4)
        self.assertRaises(TypeError, r1.update, width={"Key": 1, "Key2": 'hello'})
        self.assertRaises(TypeError, r1.update, height={"Key": 1, "Key2": 'hello'})
        self.assertRaises(TypeError, r1.update, x={"Key": 1, "Key2": 'hello'})
        self.assertRaises(TypeError, r1.update, y={"Key": 1, "Key2": 'hello'})

    def test_updateKwarg0(self):
        """Test kwarg with 0"""
        r1 = Rectangle(3, 4)
        self.assertRaises(ValueError, r1.update, width=0)
        self.assertRaises(ValueError, r1.update, height=0)

    def test_updateKwargTuples(self):
        """Test kwarg with negatives"""
        r1 = Rectangle(3, 4)
        self.assertRaises(ValueError, r1.update, width=-8)
        self.assertRaises(ValueError, r1.update, height=-8)
        self.assertRaises(ValueError, r1.update, x=-8)
        self.assertRaises(ValueError, r1.update, y=-8)
