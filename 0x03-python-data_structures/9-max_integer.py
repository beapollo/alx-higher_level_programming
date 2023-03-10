#!/usr/bin/python3
def max_integer(my_list=[]):
    len = 0
    i = 0
    for item in my_list:
        len += 1
    if len == 0:
        return None
    max = my_list[0]
    while i < len:
        if max < my_list[i]:
            max = my_list[i]
        i += 1
    return max
