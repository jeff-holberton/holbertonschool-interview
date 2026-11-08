#!/usr/bin/python3
"""n queens problem"""

import sys


def is_diagonal(x, y, current_square):
    """check for any other queens on diagonal"""
    if current_square[0] < x:
        x_diff = x - current_square[0]
    else:
        x_diff = current_square[0] - x
    if current_square[1] < y:
        y_diff = y - current_square[1]
    else:
        y_diff = current_square[1] - y
    if y_diff == x_diff:
        return True
    return False


def can_attack(current_list, current_square):
    """checks if the current placement of a queen can be attacked"""
    for _list in current_list:
        x = _list[0]
        y = _list[1]
        if x == current_square[0]:
            return True
        if y == current_square[1]:
            return True
        if is_diagonal(x, y, current_square):
            return True
    return False


def nqueens(N):
    """solves the nqueens problem"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        return 1
    if isinstance(N, int) is False:
        print("N must be a number")
        return 1
    if N < 4:
        print("N must be at least 4")
        return 1

    for _ in range(N):
        for _ in range(N):
            print("[]", end="")
        print()

    solutions = []
    current = []

    def place(row):
        if row == N:
            solutions.append(current.copy())
            return
        for col in range(N):
            if not can_attack(current, [row, col]):
                current.append([row, col])
                place(row + 1)
                current.pop()

    place(0)
    return solutions
