#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return 0
    div = sum(j for i, j in my_list)
    product = (a * b for a, b in my_list)
    sum1 = 0
    for val in product:
        sum1 += val
    total = 0
    total = sum1 / div
    return total
