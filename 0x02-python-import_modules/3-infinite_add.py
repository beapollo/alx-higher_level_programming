#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    n = len(argv) - 1
    if (n > 0):
        i = 1
        sum = 0
        while i <= n:
            sum += int(argv[i])
            i += 1
    print("{:d}".format(sum))
