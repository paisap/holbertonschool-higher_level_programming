#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value=None):
        if value is None:
            Base.__nb_objects += 1
            self.__id = self.__nb_objects
        else:
            self.__id = value

    def to_json_string(list_dictionaries):
        if len(list_dictionaries) <= 0 or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
