#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    t = 0
    try:
        my_list[x - 1]
        for i in range(x):
            print('{:d}'.format(my_list[i]), end="")
        print()
        return x

    except IndexError:
        for i in my_list:
            print('{:d}'.format(i), end="")
            t += 1
        print()
        return t
