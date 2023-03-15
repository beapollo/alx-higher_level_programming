#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    sum = 0
    for x in my_list:
        if x not in unique_list:
            unique_list.append(x)
            sum += x
    return(sum)
