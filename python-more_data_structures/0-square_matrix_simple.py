#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix by squaring each element using a list comprehension
    return [[elem**2 for elem in row] for row in matrix]
