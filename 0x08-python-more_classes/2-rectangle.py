#!/usr/bin/python3
"""
A class rectangle that defines a rectangle (based on 1-rectangle.py)
"""


class Rectangle:
    """defines a class Rectangle"""

    def __init__(self, width=0, height=0):
        """initialization of fields"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrive the attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the value for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives the attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the value for height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Gets the area of the rectangle"""
        return ((self.__width * self.__height))

    def perimeter(self):
        """Gets the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (self.__width * 2 + self.__height * 2)
