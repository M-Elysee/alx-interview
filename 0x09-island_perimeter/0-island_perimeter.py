#!/usr/bin/python3
"""
    This module containes a function island_perimeter
       - accepts one arugment (grid)
       - the grid is in a form of 2D matrics
       - 0 represents water and 1 represents land
       - Each cell is square, with a side length of 1
       - returns the perimeter of the island described in the grid
"""


def island_perimeter(grid):
    """
        - a function that takes grid as an argument
        - returns the perimeter of an island on the grid represented
        as 1 in the matrix
    """
    p = 0
    if type(grid) != list:
        return 0
    x = len(grid)
    for i, row in enumerate(grid):
        y = len(row)
        for j, col in enumerate(row):
            if col == 0:
                continue
            sides = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == y - 1 or (y > j + 1 and row[j + 1] == 0),
                i == x - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            p += sum(sides)
    return p
