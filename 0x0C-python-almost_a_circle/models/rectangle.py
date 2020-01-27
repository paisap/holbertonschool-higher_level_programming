#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Class Base with the attributes for the other class
that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """ Class Rectanagle """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ ... """
        return self.__height

    @height.setter
    def height(self, value):
        """ ... """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """ ... """
        return self.__y

    @y.setter
    def y(self, value):
        """ ... """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """ ... """
        return self.__x

    @x.setter
    def x(self, value):
        """ ... """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """ ... """
        return self.__width * self.__height

    def display(self):
        """ ... """
        for i in range(self.__height):
            print("{}".format('#') * self.__width)

    def __str__(self):
        """ ... """
        return "[{}] ({}) {}/{} - {}/{}".format(
            __class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def display(self):
        """ ... """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(' ' * self.__x, '#' * self.__width))

    def update(self, *args, **kwargs):
        """ ... """
        if args != ():
            j = 0
            for i in args:
                if j == 0:
                    super().__init__(i)
                if j == 1:
                    self.width = i
                if j == 2:
                    self.height = i
                if j == 3:
                    self.x = i
                if j == 4:
                    self.y = i
                j += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ ... """
        new = {}
        new['id'] = self.id
        new['width'] = self.width
        new['height'] = self.height
        new['x'] = self.x
        new['y'] = self.y
        return new
