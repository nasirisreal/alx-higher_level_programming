#!/usr/bin/python3

"""
This module contains an algorithm that resolves the N-Queen puzzle
using backtracking and a matrix to represent the chessboard
"""

def isSafe(board, row, col, n):
    """ Method that determines if the queens can or can't kill each other

    Args:
        board: matrix that represents the chessboard
        row: current row being checked
        col: current column being checked
        n: size of the chessboard

    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill
    """
    # Check rows on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_result(board):
    """ Method that prints the matrix with the Queens positions

    Args:
        board: matrix that represents the chessboard
    """
    res = [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == 1]
    print(res)


def Queen(board, col, n):
    """ Recursive function that executes the Backtracking algorithm

    Args:
        board: matrix that represents the chessboard
        col: current column being checked
        n: size of the chessboard
    """
    if col == n:
        print_result(board)
        return True

    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1

            if Queen(board, col + 1, n) is True:
                return True

            board[i][col] = 0

    return False


def solveNQueens(size):
    """ Function that invokes the Backtracking algorithm

    Args:
        size: size of the chessboard
    """
    board = [[0 for j in range(size)] for i in range(size)]

    if Queen(board, 0, size) is False:
        print("Solution does not exist")


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solveNQueens(size)

