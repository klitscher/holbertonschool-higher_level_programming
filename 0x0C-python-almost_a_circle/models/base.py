#!/usr/bin/python3
"""Module for creating a base class"""


import json
import os.path


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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy = cls(1, 2, 3, 4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        lis = []
        if not os.path.isfile(cls.__name__ + ".json"):
            return lis
        with open(cls.__name__ + ".json", encoding="utf-8") as myFile:
            json_str = myFile.read()
        my_dict = cls.from_json_string(json_str)
        for inst in my_dict:
            lis.append(cls.create(**inst))
        return lis
