#!/usr/bin/python3
"""Method to create a student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of student"""
        li = self.__dict__
        dic = {}
        for key, value in li.items():
            if isinstance(value, list) or isinstance(
                    value, dict) or isinstance(
                        value, str) or isinstance(
                            value, int) or isinstance(value, bool):
                dic.update({key: value})
        return dic
