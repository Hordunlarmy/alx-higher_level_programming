#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, operator):
        """Changes the behaviour of == opeartor with != """
        return self.before != operator

    def __ne__(self, operator):
        """Changes the behaviour of != operator with == """
        return self.before == operator
