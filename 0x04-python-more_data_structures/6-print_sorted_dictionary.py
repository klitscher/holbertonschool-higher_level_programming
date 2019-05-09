#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d = sorted(a_dictionary.items())
    for i in d:
        print("{}: {}".format(i[0], i[1]))
