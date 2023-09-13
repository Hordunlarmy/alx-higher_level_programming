#!/usr/bin/python3
"""
Pascal's Triangle Program
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal triangle of n.
    """
    my_list = []
    if n <= 0:
        return my_list

    for j in range(n):
        row = [1]
        if my_list:
            prev_row = my_list[-1]
            for i in range(1, j):
                row.append(prev_row[i - 1] + prev_row[i])
            row.append(1)
        my_list.append(row)

    return my_list
