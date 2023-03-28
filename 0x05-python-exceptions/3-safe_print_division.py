#!/usr/bin/python3
def safe_print_division(a, b):
    q = None
    try:
        q = a/b
        print("Inside result: ", end="")
        return q
    except ZeroDivisionError:
        print("Inside result: ", end="")
        return None
    finally:
        print("{}".format(q))
