#!/usr/bin/python3
n = 1


def magic_string():
    global n
    hol = "Holberton, "
    hol = hol * n
    n += 1
    return hol
