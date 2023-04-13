#!/usr/bin/python3
"""
Test
"""
from typing import List

def pascal_triangle(n: int) -> List[List[int]]:
    """
    Returns a list of lists representing the first n rows of Pascal's triangle.
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

if __name__ == "__main__":
    triangle = pascal_triangle(0)
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
