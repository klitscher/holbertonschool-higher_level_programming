#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {a: x*2 for a, x in a_dictionary.items()}
    return new_dict
