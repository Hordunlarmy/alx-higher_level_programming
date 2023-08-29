#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """Square class Initialized"""
    def __init__(self, size=0):
        """ Object Size Initialized"""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        return (self.__size ** 2)
