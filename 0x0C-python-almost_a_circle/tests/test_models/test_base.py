#!/usr/bin/python3
"""Module to test Base class"""


import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """Tests for Base class"""

    def test_idCount(self):
        """Test that the id counter works"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_noArgs(self):
        """Test no argumetns"""
        b1 = Base()
        self.assertEqual(b1.id, 4)

    def test_multiArgs(self):
        """Test multiple arguments"""
        self.assertRaises(TypeError, Base, 'Hello', 1)

    def test_intArgs(self):
        """Test int args"""
        b1 = Base(5)
        self.assertEqual(b1.id, 5)

    def test_floatArgs(self):
        """Test float args"""
        b1 = Base(4.78)
        self.assertEqual(b1.id, 4.78)

    def test_expressionArg(self):
        """Test expression argument"""
        b1 = Base(3 * 8)
        self.assertEqual(b1.id, 24)

    def test_strArg(self):
        """Test string argument"""
        b1 = Base('Hello')
        self.assertEqual(b1.id, 'Hello')

    def test_listArg(self):
        """Test list as argument"""
        b1 = Base([1, 2, 3])
        self.assertEqual(b1.id, [1, 2, 3])

    def test_tupleArgs(self):
        """Test tuples as arguments"""
        b1 = Base((1, 2, 3))
        self.assertEqual(b1.id, (1, 2, 3))

    def test_dictArgs(self):
        """Test dict as arguments"""
        b1 = Base({"Key": 'value', "key2": 3})
        self.assertEqual(b1.id, {"Key": 'value', "key2": 3})
