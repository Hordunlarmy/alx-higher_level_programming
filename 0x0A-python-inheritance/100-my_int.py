#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Changes the behaviour of == opeartor with != """
        return self.real != value

    def __ne__(self, value):
        """Changes the behaviour of != operator with == """
        return self.real == value
