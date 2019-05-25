#!/usr/bin/python3
"""Module to multiply two matrices together"""


def matrix_mul(m_a, m_b):
    """Function to multiply matrices together"""

    # Check if matrices are lists
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    # Check if matrices are lists of lists in in m_a and m_b
    for list_a in m_a:
        if not isinstance(list_a, list):
            raise TypeError("m_a must be a list of lists")
    for list_b in m_b:
        if not isinstance(list_b, list):
            raise TypeError("m_a must be a list of lists")

    # Check if m_a or m_b are empty
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    # Check if lists in list are empty
    for list_1 in m_a:
        if len(list_1) == 0:
            raise ValueError("m_a can't be empty")
    for list_2 in m_b:
        if len(list_2) == 0:
            raise ValueError("m_b can't be empty")

    # Check if element of list is an int or float
    for lis_a in m_a:
        for val_a in lis_a:
            if not isinstance(val_a, int) and not isinstance(val_a, float):
                raise TypeError("m_a should contain only integers or floats")
    for lis_b in m_b:
        for val_b in lis_b:
            if not isinstance(val_b, int) and not isinstance(val_b, float):
                raise TypeError("m_b should contain only integers or floats")

    # Check if the rows are the same size
    length_a = len(m_a[0])
    for lis_1 in m_a:
        if length_a != len(lis_1):
            raise TypeError("each row of m_a must should be of the same size")
    length_b = len(m_b[0])
    for lis_2 in m_b:
        if length_b != len(lis_2):
            raise TypeError("each row of m_b must should be of the same size")

    # Check if the row of m_a is equal to the col of m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row_a = len(m_a)
    col_a = len(m_a[0])
    col_b = len(m_b[0])
    product = [[0 for row in range(col_b)] for col in range(row_a)]
    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                product[i][j] += m_a[i][k] * m_b[k][j]
    return product
