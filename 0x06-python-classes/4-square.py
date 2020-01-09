#!/usr/bin/python3
class Square:
    """Exceptions are documented in the same way as classes.

   The __init__ created a square.


    Attributes:
        size (int): Human readable string describing the exception.

    """

    def __init__(self, size=0):
        """Example of square on the __init__ method.

            Args:
            int (int): is a size of square.
        """
        if type(size) is not int:
            raise ValueError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise ValueError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value
