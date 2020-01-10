#!/usr/bin/python3
class Square:
    """Exceptions are documented in the same way as classes.

   The __init__ created a square.


    Attributes:
        size (int): Human readable string describing the exception.

    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Example of square on the __init__ method.

            Args:
            int (int): is a size of square.
        """
        if type(value) is not int:
            raise ValueError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.___size == 0:
            print()
        else self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for h in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
