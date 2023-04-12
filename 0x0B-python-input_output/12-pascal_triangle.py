#!/usr/bin/python3

def pascal_triangle(n):
    """Returns a matrix of n rows containing the values of Pascal's triangle.

    Args:
        n (int): Number of rows in the matrix.

    Returns:
        list of lists: A matrix of n rows containing the values of Pascal's triangle.
    """
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

print(pascal_triangle(5))
