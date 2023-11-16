#!/usr/bin/python3
"""
0-rotate_2d_matrix.py
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

  * Prototype: def rotate_2d_matrix(matrix):
  * Do not return anything. The matrix must be edited in-place.
  * You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    for layer in range(n // 2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            top = matrix[first][i]
            matrix[first][i] = matrix[last - (i - first)][first]
            matrix[last - (i - first)][first] = \
                matrix[last][last - (i - first)]
            matrix[last][last - (i - first)] = matrix[i][last]
            matrix[i][last] = top
