#!/usr/bin/python3
class Rectangle:
    """Exceptions are documented in the same way as classes.
        The __init__ created a rectangle.
        Attributes:
        width (int): the width of rectangle.
        height (int): the height of rectangle
    """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__height + self.__width)

    def __str__(self):
        print_str = ""
        if self.__height == 0 or self.__width == 0:
            return print_str
        for i in range(self.__height):
            for j in range(self.__width):
                print_str += "#"
            if (i + 1) != self.__height:
                print_str += "\n"
        return print_str
