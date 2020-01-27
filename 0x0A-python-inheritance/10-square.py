#!/usr/bin/python3
""" class baseGeometry
"""


class BaseGeometry:
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.integer_validator(width, height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[" + __class__.__name__ + "] " + str(self.__width) \
            + "/" + str(self.__height)


class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)
