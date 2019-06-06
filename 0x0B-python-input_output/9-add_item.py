#!/usr/bin/python3
"""Module to add arguments to python list"""
import sys
import os.path


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if os.path.isfile("./add_item.json"):
    jstring = load_from_json_file("add_item.json")
    li = sys.argv[1:len(sys.argv)]
    fullstr = jstring + li
    save_to_json_file(fullstr, "add_item.json")
else:
    li = sys.argv[1:len(sys.argv)]
    save_to_json_file(li, "add_item.json")
