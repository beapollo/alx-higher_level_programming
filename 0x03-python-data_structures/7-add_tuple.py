#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = 0
    la = 0
    lb = 0

    list_a = list(tuple_a)
    list_b = list(tuple_b)
    for item_a in tuple_a:
        la += 1
    for item_b in tuple_b:
        lb += 1

    sum = []
    while i < 2:
        if i >= la:
            list_a.append(0)
        if i >= lb:
            list_b.append(0)
        sum.append(list_a[i] + list_b[i])
        i += 1
    sum = tuple(sum)
    return sum
