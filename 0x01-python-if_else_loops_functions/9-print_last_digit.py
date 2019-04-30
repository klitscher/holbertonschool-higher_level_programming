#!/usr/bin/python
def print_last_digit(number):
    if number < 0:
        digit = (number * -1) % 10
        print("{:d}".format(digit), end="")
        return (digit)
    else:
        digit = number % 10
        print("{:d}".format(digit), end="")
        return (digit)
