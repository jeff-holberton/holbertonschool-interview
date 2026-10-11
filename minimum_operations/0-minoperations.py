#!/usr/bin/python3
import math


def findDivisor(n):
    if n == 1:
        return 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return n // i
    return 1


def minOperations(n):
    if n <= 0:
        return 0
    copy = 0
    paste = 0
    current_n = n
    while current_n != 1:
        previous_n = current_n
        current_n = findDivisor(current_n)
        if current_n == 1:
            paste += previous_n // 1
        else:
            copy += 1
            paste += 1
    return copy + paste
