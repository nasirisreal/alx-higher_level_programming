#!/usr/bin/python3

def pascal_triangle(n):
    """Returns a matrix of n rows containing the values of Pascal's triangle.

    Args:
        n (int): Number of rows in the matrix.

    Returns:
        list of lists: A matrix of n rows containing the values of Pascal's triangle.
    """
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
        return n>=1
    pascal_triangle(5) 
