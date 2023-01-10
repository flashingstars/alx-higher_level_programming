#!/usr/bin/python3
"""A module that adds all arguments to a Python list
    and saves them to a file"""
import sys


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file
args = sys.argv[1:]
jsonfile = "add_item.json"
try:
    my_list = load(jsonfile)
except FileNotFoundError:
    save(args, jsonfile)
else:
    my_list.extend(args)
    save(my_list, jsonfile)
