#!/usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """Square class initialized"""

    def __init__(self, size=0):
        """ Object size defined"""
        if type(size) is int:
            pass
        else:
            raise TypeError("size must be an integer")
        if (size >= 0):
            self.__size = size
        else:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)
