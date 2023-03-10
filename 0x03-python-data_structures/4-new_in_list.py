#!/usr/bin/python3
def new_in_list(list, index, ne):
    new = []
    n = len(list)
    i = 0
    if index >= 0 and index < n:
        while i < n:
            if i == index:
                new.append(ne)
            else:
                new.append(list[i])
            i += 1
        return(new)
    else:
        return(list)
