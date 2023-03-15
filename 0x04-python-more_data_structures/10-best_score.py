#!/usr/bin/python3
def best_score(dict):
    score = 0
    key = ''
    if not dict:
        return None
    for i in dict.keys():
        if score <= dict[i]:
            score = dict[i]
            key = i
    return key
