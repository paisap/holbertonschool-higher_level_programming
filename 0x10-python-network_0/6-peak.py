#!/usr/bin/python3
def find_peak(list_of_integers):
    """ ....."""
    if list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    return find_peak(list_of_integers[1:-1])
