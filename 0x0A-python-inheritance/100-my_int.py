#!/usr/bin/python3
"""Module to take over the int domain!"""


class MyInt(int):
    """Class to replace how int sees things"""

    def __eq__(self, other):
        """Reverse the == operator"""
        return super().__ne__(self)

    def __ne__(self, other):
        """Reverse the != operator"""
        return super().__eq__(self)
