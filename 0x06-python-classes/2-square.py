#!/usr/bin/python3
"""A class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """Defined Square Class"""

    def __init__(self, size=0):
        """object size initialized"""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')

        self.__size = size
