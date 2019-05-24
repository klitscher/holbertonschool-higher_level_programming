#!/usr/bin/python3
"""Module to practice using unittest"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class"""

    def test_empty(self):
        """Test empty list"""
        li = []
        self.assertIsNone(max_integer(li))

    def test_multipleArguments(self):
        """Test too many arguments"""
        li = [1, 2, 3, 4]
        li2 = [1, 2, 3]
        li3 = [1, 2]
        self.assertRaises(TypeError, max_integer, li, li2, li3)

    def test_oneInt(self):
        """Test only one int"""
        li = [8]
        self.assertEqual(max_integer(li), 8)

    def test_allInt(self):
        """Test all ints"""
        li = [1, 3, 7, 9]
        self.assertEqual(max_integer(li), 9)

    def test_intString(self):
        """Test int and string"""
        li = [1, 2, 3, "Hello"]
        self.assertRaises(TypeError, max_integer, li)

    def test_allStrings(self):
        """Test all strings"""
        li = ["lf", "oo", "ll", "He"]
        self.assertEqual(max_integer(li), "oo")

    def test_intFloat(self):
        """Test ints and floats"""
        li = [1, 2, 3, 4.6]
        self.assertEqual(max_integer(li), 4.6)

    def test_allFloat(self):
        """Test all floats"""
        li = [1.7, 22.6, 3.7, 4.6]
        self.assertEqual(max_integer(li), 22.6)

    def test_tuple(self):
        """Test tuples"""
        li = (1, 2, 3)
        self.assertEqual(max_integer(li), 3)

    def test_twoLists(self):
        """Test if list of list works"""
        li = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(max_integer(li), [4, 5, 6])
