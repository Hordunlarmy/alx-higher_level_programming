#!/usr/bin/python3
"""
A function that adds two integers
"""


def add_integer(a, b=98):
    """
    a and b must be integers or floats, otherwise raise a TypeError
    """

    if (type(a) not in (int, float)):
        raise TypeError("a must be an integer")
    if (type(b) not in (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
