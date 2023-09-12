#!/usr/bin/python3
"""
A class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """Class definition"""

    def area(self):
        """raise an error"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        Child of BaseGeometry
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
