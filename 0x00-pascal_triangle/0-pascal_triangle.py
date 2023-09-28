#!/usr/bin/python3
"""
0-pascal_triangle.py
This module contains the function pascal_triangle,
returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Pascal's Triangle"""
    if n <= 0:
        return []

    pascal_tri = [[1]]

    for i in range(1, n):
        prev_row = pascal_tri[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        pascal_tri.append(new_row)

    return pascal_tri
