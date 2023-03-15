#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    dict_romans = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000}
    i = 0
    n = 0
    while i < len(roman_string):
        if i > 0 and dict_romans[roman_string[i]] > dict_romans[roman_string[i - 1]]:
            n += dict_romans[roman_string[i]] - 2 * dict_romans[roman_string[i - 1]]
        else:
            n += dict_romans[roman_string[i]]
        i += 1
    return n
