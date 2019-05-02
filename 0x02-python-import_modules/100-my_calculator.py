#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div
    from sys import argv
    length = len(argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    operators = "+", "-", "*", "/"
    if op in operators:
        for i in range(len(operators)):
            if op == operators[0]:
                print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b)))
                break
            if op == operators[1]:
                print("{:d} {} {:d} = {:d}".format(a, op, b, sub(a, b)))
                break
            if op == operators[2]:
                print("{:d} {} {:d} = {:d}".format(a, op, b, mul(a, b)))
                break
            if op == operators[3]:
                print("{:d} {} {:d} = {}".format(a, op, b, div(a, b)))
                break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
