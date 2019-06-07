#!/usr/bin/python3
"""Method for a pascal function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the pascals triangle of n
    """
    ll= []
    li = [1]
    if n <= 0:
        return ll
    for row in range(1, n + 1):
        temp = li
        li = [1]
        for col in range(row):
            if col == 0:
                continue
            if col + 1 == row:
                li.append(1)
                continue
            li.append(temp[col - 1] + temp[col])
        ll.append(li)
    return ll
