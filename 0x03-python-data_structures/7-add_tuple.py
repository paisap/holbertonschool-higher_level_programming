#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2, b1, b2 = 0, 0, 0, 0
    if (len(tuple_b) == 0):
        a1 = 0
        a2 = 0
    elif (len(tuple_b) == 1):
        a1 = tuple_b[0]
        a2 = 0
    else:
        a1 = tuple_b[0]
        v_a2 = tuple_b[1]
    if (len(tuple_a) == 0):
        b1 = 0
        b2 = 0
    elif (len(tuple_a) == 1):
        b1 = tuple_a[0]
        b2 = 0
    else:
        b1 = tuple_a[0]
        b2 = tuple_a[1]
    tuple_c = (b1 + a1, b2 + a2)
    return tuple_c
