#!/usr/bin/python3
def find_peak(list_of_integers):
    """ ....."""
    if list_of_integers is None or len(list_of_integers) is 0:
        return None
    if len(list_of_integers) < 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    j = 0
    t = len(list_of_integers) - 2
    for i in range(len(list_of_integers) - 1, -1, -1):
        if list_of_integers[i] >= list_of_integers[t] and \
                list_of_integers[i] >= list_of_integers[j]:
            return list_of_integers[i]
        j += 1
        t -= 1
    return None
