#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            __class__.__name__, self.id, self.x, self.y,
            self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args != ():
            j = 0
            for i in args:
                if j == 0:
                    self.id = i
                if j == 1:
                    self.size = i
                if j == 2:
                    self.x = i
                if j == 3:
                    self.y = i
                j += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        new = {}
        new['id'] = self.id
        new['size'] = self.size
        new['x'] = self.x
        new['y'] = self.y
        return new
