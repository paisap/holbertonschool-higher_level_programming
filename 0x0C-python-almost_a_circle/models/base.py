#!/usr/bin/python3
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
