#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) <= 0 or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "" + cls.__name__ + ".json"
        text = []
        with open(filename, mode='w', encoding='UTF-8') as f:
            if list_objs is None:
                text = []
            else:
                for i in list_objs:
                    text.append(i.to_dictionary())
                json_list = cls.to_json_string(text)
            f.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) <= 0:
            return []
        return json.loads(json_string)
