#!/usr/bin/python3
"""
Base Class
"""
import json


class Base:
    """Class Defined"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization phase"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)
