#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = [key for key, val in a_dictionary.items() if val is value]
    for key in new:
        del a_dictionary[key]
    return a_dictionary
