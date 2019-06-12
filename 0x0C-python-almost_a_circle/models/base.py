#!/usr/bin/python3
"""Module for creating a base class"""


import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns Json representation of a dict"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json str representation to file"""

        lis = []
        if list_objs is None:
            with open(cls.__name__ + ".json", encoding="utf-8",
                      mode="a+") as myFile:
                myFile.write(lis)
        else:
            for li in list_objs:
                lis.append(li.to_dictionary())
            js_dic = cls.to_json_string(lis)
            with open(cls.__name__ + ".json", encoding="utf-8",
                      mode="a+") as myFile:
                myFile.write(js_dic)

    @staticmethod
    def from_json_string(json_string):
        """Convert json string to list of dicts"""
        lis = []
        # not sure if empty means empty string or len(jstr) < 1
        if json_string is None or json_string == "":
            return lis
        return json.loads(json_string)
