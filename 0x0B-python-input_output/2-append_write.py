#!/usr/bin/python3
"""A module that defines a file appending function."""


def append_write(filename, text=""):
    """Appends a string to the end of a UTF8 textfile"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
