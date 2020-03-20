#!/usr/bin/python3
class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dictt = self.__dict__
        new = {}
        if attrs is not None:
            for i in attrs:
                if i in dictt:
                    new[i] = dictt[i]
            return new
        return dictt
