#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None or type(roman_string) != str:
        return 0
    dic_rom = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000}
    i = 0
    n = 0
    while i < len(roman_string):
        if i > 0 and dic_rom[roman_string[i]] > dic_rom[roman_string[i - 1]]:
            n += dic_rom[roman_string[i]] - 2 * dic_rom[roman_string[i - 1]]
        else:
            n += dic_rom[roman_string[i]]
        i += 1
    return n
