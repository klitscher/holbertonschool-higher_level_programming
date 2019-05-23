#!/usr/bin/python3
"""Module to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """function to divide the matrix

    Has many error casses needed to be accounted for
    """

    # Check if matrix is not a list of lists containing ints or floats
    err1 = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(matrix, list):
        raise TypeError(err1)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(err1)
        for val in lists:
            if not isinstance(val, int) and not isinstance(val, float):
                raise TypeError(err1)

    # Check if length of lists in matrix are not equal
    length = len(matrix[0])
    for list_size in matrix:
        if length != len(list_size):
            raise TypeError('Each row of the matrix must have the same size')

    # Check if div is not a float/int or if it is zero
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new = [[round((matrix[x][i]/div), 2) for i in range(
        len(matrix[x]))] for x in range(len(matrix))]
    print(new)
