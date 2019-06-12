#!/usr/bin/python3
"""Module for creating a base class"""


import json
import os.path
import turtle


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
            js_dic = cls.to_json_string(lis)
            with open(cls.__name__ + ".json", encoding="utf-8",
                      mode="w") as myFile:
                myFile.write(js_dic)
        else:
            for li in list_objs:
                lis.append(li.to_dictionary())
            js_dic = cls.to_json_string(lis)
            with open(cls.__name__ + ".json", encoding="utf-8",
                      mode="w") as myFile:
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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
            dummy.update(**dictionary)
            return dummy
        if cls.__name__ == "Square":
            dummy = cls(1)
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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw a square with turtle"""
        window = turtle.Screen()
        turts = turtle.Turtle()
        if len(list_rectangles) > 0:
            for rect in list_rectangles:
                turts.forward(rect.height)
                turts.right(90)
                turts.forward(rect.width)
                turts.rigth(90)
                turts.forward(rect.height)
                turts.right(90)
                turts.forward(rect.width)
                turts.right(90)
        if len(list_squares) > 0:
            for sq in list_squares:
                turts.forward(sq.height)
                turts.right(90)
                turts.forward(sq.width)
                turts.rigth(90)
                turts.forward(sq.height)
                turts.right(90)
                turts.forward(sq.width)
                turts.right(90)

        window.exitonclick()
