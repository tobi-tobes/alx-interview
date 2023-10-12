#!/usr/bin/python3
"""
0-minoperations.py
In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste. Given
a number n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if n < 2:
        return 0

    clipboard = 0
    no_of_ops = 0
    text_length = 1

    while text_length < n:
        if n % text_length == 0:
            clipboard = text_length
            no_of_ops += 1
        text_length += clipboard
        no_of_ops += 1

    return no_of_ops
