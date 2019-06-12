#!/usr/bin/python3
"""Module to test Base class"""


import unittest
from unittest import mock
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    """Tests for Base class"""

    #----------------Tests general----------------------------

    def test_idCount(self):
        """Test that the id counter works"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)

    #----------------Tests arguments----------------------------

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

    #----------------Tests to_json_string----------------------------

    def test_toJsonStrWorks(self):
        """Test that it works"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        d1 = {'x': 2, 'width': 10, 'id': r1.id , 'height': 7, 'y': 8}
        self.assertDictEqual(dictionary, d1)
        self.assertTrue((type(dictionary) is dict))
        self.assertTrue((type(json_dictionary) is str))

    def test_toJsonStr2Args(self):
        """Test with 2 args"""
        r1 = Rectangle(10, 7, 2, 8)
        di = r1.to_dictionary()
        self.assertRaises(TypeError, Base.to_json_string, [di], 1)

    #----------------Tests save_to_file----------------------------

    #Need Tests for this

    #----------------Tests from_json_string----------------------------

    def test_fromJsonStringEmpty(self):
        """Test empty input"""
        li = []
        json_list_input = ""
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(li, list_output)

    def test_fromJsonStringNone(self):
        """Test None input"""
        li = []
        json_list_input = None
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(li, list_output)

    def test_fromJsonStringNoArgs(self):
        """Test no arguments"""
        li = []
        json_list_input = None
        self.assertRaises(TypeError, Rectangle.from_json_string)

    def test_fromJsonStringTooManyArgs(self):
        """Test too many arguments"""
        li = []
        json_list_input = None
        self.assertRaises(TypeError, Rectangle.from_json_string, 1, 2)

    #Need more Tests for this?
