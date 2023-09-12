#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ function definition"""

    with open(filename, encoding="utf-8", mode="w") as myFile:
        myFile.write(text)

    with open(filename, encoding="utf-8") as myFile:
        return len(myFile.readline())
