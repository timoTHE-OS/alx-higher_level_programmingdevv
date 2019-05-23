#!/usr/bin/python3
"""
Module matrix_divided
Divides each element of a matrix of numbers by a number
"""


def matrix_divided(matrix, div):
    """Returns a new matrix (list of list)
    with the result of the division of matrix by div
    rounded to 2 decimal places.
    """

    for row in matrix:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
