#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    b_dictionary.update({n: 2 * b_dictionary[n] for n in b_dictionary.keys()})
    return b_dictionary
