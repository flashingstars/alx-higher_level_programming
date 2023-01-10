#!/usr/bin/python3
"""A module that defines a file writing function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
