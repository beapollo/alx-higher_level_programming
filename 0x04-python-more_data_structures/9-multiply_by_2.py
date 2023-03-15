#!/usr/bin/python3
def multiply_by_2(dict):
    new_dict = {}
    for i in dict.keys():
        new_dict[i] = 2 * dict[i]
    return(new_dict)
