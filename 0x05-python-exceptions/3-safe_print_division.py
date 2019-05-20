#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = 0
    try:
        quotient = a / b
        return quotient
    except ZeroDivisionError:
        return None
    finally:
        if b == 0:
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {:.1f}".format(quotient))
