#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] == '+' or argv[2] == '-' or argv[2] == '*' or argv[2] == '/':
        n1 = int(argv[1])
        n2 = int(argv[3])
        result = 0
        if argv[2] == '+':
            result = add(n1, n2)
        elif argv[2] == '-':
            result = sub(n1, n2)
        elif argv[2] == '*':
            result = mul(n1, n2)
        elif argv[2] == '/':
            result = div(n1, n2)
        print("{:d} {:s} {:d} = {:d}".format(n1, argv[2], n2, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
