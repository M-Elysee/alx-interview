#!/usr/bin/python3
"""a program that prints all possible formations of N non-attacking
   queens in an NxN chessboard"""


def board(n):
    """a function that creates an NxN matrix"""
    return [[0] * n for _ in range(n)]


def print_formation(board, n):
    """ a funtion that prints the possible non-attaching formations of
       queens  on a chessboard"""
    m = [[i, y] for i in range(n) for y in range(n) if board[i][y] == 1]
    print(m)


def is_safe(board, row, col, n):
    """a function that find the safe row for the queen where it can not be
       attacked"""

    # checking the left row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # checking the upper left diagonal
    for i, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][y] == 1:
            return False
    # checking the lower diagonal
    for i, y in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][y] == 1:
            return False
    return True


def nqueens(board, col, n):
    """a function that find n non-attacking queens formation in a chess
       board"""
    # establishing the end point of our recursion
    if col >= n:
        return True

    # browsing and assigning appropiate values on each slot of the board
    for row in range(n):
        if (is_safe(board, row, col, n)):
            board[row][col] = 1
            if (nqueens(board, col + 1, n)):
                print_formation(board, n)
                board[row][col] = 0
                continue
            board[row][col] = 0
    return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)

    board = board(n)
    nqueens(board, 0, n)
