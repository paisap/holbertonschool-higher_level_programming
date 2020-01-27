#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Class Base with the attributes for the other class
that inherits from Base
"""

import json


class Base:
    """ class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ ..."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ ..."""
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
        """ ..."""
        if json_string is None or len(json_string) <= 0:
            return []
        return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ ..."""
        tmp = cls(1, 1, 1, 1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """ ..."""
        h = "" + cls.__name__ + ".json"
        text = ""
        new = []
        with open(h, "r", encoding="UTF-8") as f:
            text = f.read()
            obj = cls.from_json_string(text)
            for i in obj:
                new.append(cls.create(**i))
        return new
