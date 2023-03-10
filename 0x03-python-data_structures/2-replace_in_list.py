#!/usr/bin/python3
def replace_in_list(list, index, ne):
    n = len(list)
    if index >= 0 and index < n:
        list[index] = ne
    return(list)
