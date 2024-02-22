#!/usr/bin/python3
"""a module containing a function that rotate a 2d matrice
   90degrees clockwise
"""


def rotate_2d_matrix(matrix):
    '''it takes a matrix as an arg transform it and return nothing
    '''
    n = len(matrix[0])
    for x in range(0, int(n / 2)):
        for y in range(x, n - 1 - x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[n - 1 - y][x]
            matrix[n - 1 - y][x] = matrix[n - 1 - x][n - 1 - y]
            matrix[n - 1 - x][n - 1 - y] = matrix[y][n - 1 - x]
            matrix[y][n - 1 - x] = temp
    return
