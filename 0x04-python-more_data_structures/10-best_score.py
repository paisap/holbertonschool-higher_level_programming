#!/usr/bin/python3
def best_score(a_dictionary):
    value = 0
    string = ""
    if a_dictionary:
        for i in a_dictionary:
            if a_dictionary[i] > value:
                value = a_dictionary[i]
                string = i
        return string
    return "None"
