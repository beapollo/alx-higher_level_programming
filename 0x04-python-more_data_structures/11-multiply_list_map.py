#!/usr/bin/python3
def multiply_list_map(my_list=[], number):
    new_list = []
    for e in my_list:
        new_list.append(e * number)
    return new_list
