#!/usr/bin/python3
"""
0-nqueens.py
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard. Write a program that solves the N queens problem.

* Usage: nqueens N
    * If the user called the program with the wrong number of arguments
    print Usage: nqueens N, followed by a new line, and exit with the status 1
* where N must be an integer greater or equal to 4
    * If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
    * If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
* The program should print every possible solution to the problem
    * One solution per line
    * Format: see example
    * You don't have to print the solutions in a specific order
* You are only allowed to import the sys module
"""

import sys


def is_safe(board, row, col, n):
    """Checks whether placement of queen is safe"""
    for prev_col in range(col):
        prev_row = board[prev_col]
        if prev_row == row or \
           prev_row - (col - prev_col) == row or \
           prev_row + (col - prev_col) == row:
            return False
    return True


def print_solution(board):
    """Prints out the board"""
    solution = []
    for col in range(len(board)):
        solution.append([col, board[col]])
    print(solution)


def solve_nqueens(n):
    """Solves the N Queens problem"""
    if n < 4:
        print("N must be at least 4")
        return

    board = [-1] * n

    def solve(col):
        """Inner solving helper"""
        if col == n:
            print_solution(board)
            return

        for row in range(n):
            if is_safe(board, row, col, n):
                board[col] = row
                solve(col + 1)

    solve(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
