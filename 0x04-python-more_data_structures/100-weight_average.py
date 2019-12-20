#!/usr/bin/python3
def weight_average(my_list=[]):
    div = 0
    result = 0
    if my_list:
        for i in my_list:
            result += i[0] * i[1]
            div += i[1]
        return result / div
    return 0
