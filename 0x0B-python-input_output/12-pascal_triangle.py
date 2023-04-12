#!/usr/bin/python3

def pascal_triangle(n):
    """Returns a matrix of n rows containing the values of Pascal's triangle.

    Args:
        n (int): Number of rows in the matrix.

    Returns:
        list of lists: A matrix of n rows containing the values of Pascal's triangle.
    """
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i-1]
            for j in range(len(prev_row)-1):
                row.append(prev_row[j] + prev_row[j+1])
            row.append(1)
        triangle.append(row)
    return triangle

print(pascal_triangle(5))
