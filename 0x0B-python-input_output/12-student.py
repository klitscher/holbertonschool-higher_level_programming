#!/usr/bin/python3
"""Method to create a student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of student"""
        li = self.__dict__
        dic = {}
        dic2 = {}
        for key, value in li.items():
            if isinstance(value, list) or isinstance(
                    value, dict) or isinstance(
                        value, str) or isinstance(
                            value, int) or isinstance(value, bool):
                dic.update({key: value})
        if attrs is None:
            return dic
        elif not isinstance(attrs, list):
            return dic
        for i in attrs:
            if not isinstance(i, str):
                return dic
        for key2, val2 in dic.items():
            if key2 in attrs:
                dic2.update({key2: val2})
        return dic2
