#!/usr/bin/python3
"""A module that defines a text-reading function"""


def read_file(filename=""):
    """Prints the contents of a UTF8 taxt file"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
