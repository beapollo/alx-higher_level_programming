#!/usr/bin/python3
def simple_delete(dict, key):
    if key in dict.keys():
        dict.pop(key)
    return(dict)
