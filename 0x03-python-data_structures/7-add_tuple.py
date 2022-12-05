#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup1 = list(tuple_a)
    tup2 = list(tuple_b)
    if len(tup1) < 2:
        if len(tup1) == 1:
            tup1.append(0)
        else:
            tup1.append(0)
            tup1.append(0)
    if len(tup2) < 2:
        if len(tup2) == 1:
            tup2.append(0)
        else:
            tup2.append(0)
            tup2.append(0)
    return (tup1[0] + tup2[0]), (tup1[1] + tup2[1])
