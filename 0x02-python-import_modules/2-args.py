#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    if (n == 0):
        print("{:d} arguments.".format(n))
    elif (n == 1):
        print("{:d} argument:".format(n))
        print("{:d}: {:s}".format(n, argv[n]))
    else:
        print("{:d} arguments:".format(n))
        i = 1
        while i <= n:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
