#!/usr/bin/python3
"""
a function that returns True if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, the_class):
    "Class Definition"

    if type(obj) is the_class:
        return True
    else:
        return False
