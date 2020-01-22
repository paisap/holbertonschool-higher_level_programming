#!/usr/bin/python3


def number_of_lines(filename=""):
    j = 0
    with open(filename, encoding='UTF8') as file:
        for i in file:
            j += 1
    return j
