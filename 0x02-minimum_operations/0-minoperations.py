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
    
    clipboard = ''
    no_of_ops = 0
    text = 'H'

    while len(text) < n:
        if n % len(text) == 0:
            clipboard = text
            no_of_ops += 1
        text = text + clipboard
        no_of_ops += 1

    return no_of_ops
