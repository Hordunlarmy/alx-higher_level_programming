#!/usr/bin/python3
"""
 function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """ function definition"""
    import json

    with open(filename) as myFile:
        return (json.load(myFile))
