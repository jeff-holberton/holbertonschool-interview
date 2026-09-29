#!/usr/bin/python3
"""pascal_triangle algorithm"""


def pascal_triangle(n):
    """function"""
    if n <= 0:
        return []
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0:
                row.append(1)
                continue
            try:
                row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            except IndexError:
                row.append(1)
        triangle.append(row)
    return triangle
