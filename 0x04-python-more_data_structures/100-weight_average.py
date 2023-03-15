#!/usr/bin/python3
def weight_average(my_list=[]):
    wg_avg = 0
    div = 0
    if my_list == []:
        return 0
    for tup in my_list:
        wg_avg += tup[0] * tup[1]
        div += tup[1]
    return float(wg_avg / div)
