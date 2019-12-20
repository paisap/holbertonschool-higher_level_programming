#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = dict.copy(a_dictionary)
    for i in new:
        if new[i] == value:
            del a_dictionary[i]
    return a_dictionary
