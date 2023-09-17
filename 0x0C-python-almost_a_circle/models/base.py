#!/usr/bin/python3
"""
Base Class
"""


class Base:
    """Class Defined"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization phase"""

        if id is not None:
            self.id = id
        else:
            super().__nb_objects += 1
            self.id = super().__nb_objects
