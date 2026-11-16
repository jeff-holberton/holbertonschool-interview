#!/usr/bin/python3
"""Making change"""
    

def makeChange(coins, total):
    if total <= 0:
        return 0
    if len(coins) == 0:
        return -1
    maximum = max(coins)
    division = total // maximum
    if division > 0:
        total = total - (division * maximum)
    coins.remove(maximum)
    recursive = makeChange(coins, total)
    if recursive < 0:
        return - 1
    return division + recursive
