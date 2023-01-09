#!/usr/bin/python3
""" 
    This module returns the list of available attributes and 
    methods of an object
    """

def lookup(obj):
    """Function that looks for all attributes and methods of an object"""
    return dir(obj)
