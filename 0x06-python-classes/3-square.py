#!/usr/bin/python3
"""
This is the "Square" module.

Method area returns area of the square
"""


class Square:
    """A class that defines a square by size and compute area"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
