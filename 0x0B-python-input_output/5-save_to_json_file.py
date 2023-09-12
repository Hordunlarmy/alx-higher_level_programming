#!/usr/bin/python3
"""
a function that writes an Object to a text file
"""


def save_to_json_file(my_obj, filename):
    """writes tofile using json representation"""
    import json

    with open(filename, "w") as myFile:
        myFile.write(json.dumps(my_obj))
