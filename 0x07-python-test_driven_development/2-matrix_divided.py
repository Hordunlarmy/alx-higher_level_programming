#!/usr/bin/python3
"""
Function to divide a matrix(a 3 by 2 list)
"""


def matrix_divided(matrix, div):
    """
        Checks for conditions of the matrix and div values
        before performing division logic
    """
    for row in matrix:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError("matrix must be matrix (list of lists)\
                        of integers/floats")

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = element / div
            new_row.append(round(result, 2))
        new_matrix.append(new_row)

    return (new_matrix)
