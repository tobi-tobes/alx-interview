#!/usr/bin/python3
"""
0-island_perimeter.py
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid:

  * grid is a list of list of integers:
    * 0 represents water
    * 1 represents land
    * Each cell is square, with a side length of 1
    * Cells are connected horizontally/vertically (not diagonally).
    * grid is rectangular, with its width and height not exceeding 100
  * The grid is completely surrounded by water
  * There is only one island (or nothing).
  * The island doesn't have “lakes” (water inside
    that isn't connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    w = len(grid[0])
    h = len(grid)
    perimeter = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                surrounding = 4
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    surrounding -= 1
                if i + 1 <= h - 1 and grid[i + 1][j] == 1:
                    surrounding -= 1
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    surrounding -= 1
                if j + 1 <= w - 1 and grid[i][j + 1] == 1:
                    surrounding -= 1
                perimeter += surrounding
            else:
                continue
    return perimeter
