#!/usr/bin/python3
"""
A class rectangle that defines a rectangle  (based on 2-rectangle.py)
"""


class Rectangle:
    """defines a class rectangle"""

    def __init__(self, width=0, height=0):
        """initialization of fields"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrives the width attribute"""
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
        """retrives height attribute"""
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
        """gets the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """gets the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """returns the rectangle as #"""

        if (self.__height == 0 or self.__width == 0):
            return ("")

        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            string += "\n"
        return (string[: -1])
