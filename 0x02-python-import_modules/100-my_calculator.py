#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    slen = len(argv)
    if (slen != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = ["+", "-", "*", "/"]
    op = argv[2]
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if (op == ops[0]):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (op == ops[1]):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (op == ops[2]):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif (op == ops[3]):
        print("{} + {} = {}".format(a, b, div(a, b)))
