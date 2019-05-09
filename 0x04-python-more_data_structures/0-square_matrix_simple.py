#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    size = len(matrix[0])
    new_matrix = [[x**2 for x in ele] for ele in matrix]
    return new_matrix
