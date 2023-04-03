#!/usr/bin/env python3

import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed in a given row and column without
    attacking any other queens on the board.

    Args:
        board: The current state of the board.
        row: The row to check.
        col: The column to check.
        n: The size of the board.

    Returns:
        True if the placement is safe, False otherwise.
    """

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check if there is a queen on the diagonal up-left
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check if there is a queen on the diagonal up-right
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(n):
    """
    Find all possible solutions to the n-queens problem.

    Args:
        n: The size of the board.

    Returns:
        A list of all possible solutions, where each solution is a list of
        strings representing the board with "Q" indicating a queen and "." 
        indicating an empty square.
    """

    def backtrack(board, row):
        """
        Recursive function to place queens on the board.

        Args:
            board: The current state of the board.
            row: The current row to place a queen in.

        Returns:
            A list of all possible solutions found from this point on.
        """

        if row == n:
            # All queens have been placed, this is a solution
            return [board[:]]

        solutions = []

        for col in range(n):
            if is_safe(board, row, col, n):
                # Place a queen in this position
                board[row][col] = "Q"

                # Recursively search for solutions
                solutions += backtrack(board, row + 1)

                # Remove the queen from this position
                board[row][col] = "."

        return solutions

    # Initialize an empty board
    board = [["." for _ in range(n)] for _ in range(n)]

    # Find all possible solutions
    solutions = backtrack(board, 0)

    return solutions


if __name__ == "__main__":
    # Parse the command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the problem and print the solutions
    solutions = solve_n_queens(n)

    for solution in solutions:
        for row in solution:
            print(" ".join(row))
        print()

