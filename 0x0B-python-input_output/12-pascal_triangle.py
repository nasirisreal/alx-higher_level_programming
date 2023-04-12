#!/usr/bin/python3

def pascal_triangle(n):
    """Returns a matrix of n rows containing the values of Pascal's triangle.

    Args:
        n (int): Number of rows in the matrix.

    Returns:
        list of lists: A matrix of n rows containing the values of Pascal's triangle.
    """
    matrix = []
    prev_row = []

    for i in range(n):
        row = []
        left_index = -1
        right_index = 0
        for j in range(len(prev_row) + 1):
            if left_index == -1 or right_index == len(prev_row):
                row.append(1)
            else:
                row.append(prev_row[left_index] + prev_row[right_index])
            left_index += 1
            right_index += 1
        matrix.append(row)
        prev_row = row[:]
    
    return matrix

