#!/usr/bin/python3
class MyInt(int):
    def __init__(self, a):
        self.a = a

    def __eq__(self, other):
        if self.a == int(other):
            return False
        else:
            return True

    def __ne__(self, other):
        if self.a != int(other):
            return False
        else:
            return True
