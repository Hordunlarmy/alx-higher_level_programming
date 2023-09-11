#!/usr/bin/python3
"""
A class that inherits fron list
"""


class MyList(list):
    """Class Defination"""

    def __init__(self):
        """Class initialization"""

        super().__init__()

    def print_sorted(self):
        """
        print the sorted list
        """
        print(sorted(self))
