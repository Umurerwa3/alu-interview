#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers
representing the Pascal's triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def pascal_triangle(n):
    """
    A function def pascal_triangle(n): that returns a list of lists of integers
    representing the Pascal's triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle