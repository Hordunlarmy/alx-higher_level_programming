#!/usr/bin/python3
"""
a function that shows the JSON representation of an object
"""


def to_json_string(my_obj):
    """Returns the JSON representation of a string"""
    import json

    return (json.dumps(my_obj))
