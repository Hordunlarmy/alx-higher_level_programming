#!/usr/bin/python3
"""
a class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class defined"""

    def __init__(self, size):
        """Square class initialized"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
