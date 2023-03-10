#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len = 0
    i = 0

    for item in my_list:
        len += 1
    if idx < 0 or idx >= len:
        return my_list
    while i < len:
        if i == idx:
            del my_list[i]
        i += 1
    return my_list
