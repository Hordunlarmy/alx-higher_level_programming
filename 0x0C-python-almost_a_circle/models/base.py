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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"

        with open(file_name, "w") as jsonFile:
            if list_objs is None:
                jsonFile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonFile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return ("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                temp = cls(1, 1)
            else:
                temp = cls(1)
            temp.update(**dictionary)
            return (temp)

    @classmethod
    def load_from_file(cls):
        new_file = cls.__name__ + ".json"
        try:
            with open(new_file) as myFile:
                the_list = cls.from_json_string(myFile.read())
                return [cls.create(**dic) for dic in the_list]
        except Exception:
            return []
