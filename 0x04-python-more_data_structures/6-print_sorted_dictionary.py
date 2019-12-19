#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = []
    key = list(sorted(a_dictionary.keys()))
    for i in key:
        print('{} : {}'.format(i, a_dictionary[i]))
