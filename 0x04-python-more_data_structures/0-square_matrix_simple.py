#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # a function that computes the square value of all integers of a matrix.

    new_matrix = []

    for row in matrix:
        new_matrix.append([element ** 2 for element in row])
    return (new_matrix)
