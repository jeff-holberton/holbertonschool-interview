#!/usr/bin/python3
"""Algorithm that rotates a matrix clockwise"""


def rotate_2d_matrix(matrix):
    """Rotating matrix algorithm"""
    size = len(matrix[0])
    y = 0
    x = size - 1
    copy = [[0 for _ in range(size)] for _ in range(size)]
    for _list in matrix:
        for element in _list:
            copy[y][x] = element
            y += 1
        y = 0
        x -= 1
    for row, _list in enumerate(copy):
        for col, element in enumerate(_list):
            matrix[row][col] = element
