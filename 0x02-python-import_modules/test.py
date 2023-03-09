#!/usr/bin/python3
import sys

def count_vowels(args):
    vowels = set() 
    for arg in args:
        for char in arg:
            if char.lower() in 'aeiou':
                vowels.add(char)
    return len(vowels)

print(count_vowels(args))
