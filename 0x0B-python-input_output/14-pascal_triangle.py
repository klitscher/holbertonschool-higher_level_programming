#!/usr/bin/python3
"""Method for a pascal function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the pascals triangle of n
    """
    actual = []
    li = [1]
    if n <= 0:
        return actual
    for row in range(n):
        actual.append(li)
        new = []
        new.append(li[0])
        for col in range(len(li) - 1):
            new.append(li[col] + li[col + 1])
        new.append(li[-1])
        li = new
    return actual
