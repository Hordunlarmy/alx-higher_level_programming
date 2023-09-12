#!/usr/bin/python3
"""
a class Square that inherits from Rectangle (9-rectangle.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Defined"""

    def __init__(self, width, height):
        """Class initialized"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)


class Square(Rectangle):
    """Square class defined."""

    def __init__(self, size):
        """Square class initialized."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
