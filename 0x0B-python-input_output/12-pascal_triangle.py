#!/usr/bin/python3

def pascal_triangle(n):
    """ Function that returns the pascal triangle

    Args:
        n: number of lines

    Returns:
        matrix: a matrix with the pascal triangle

    """
    trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(5)
