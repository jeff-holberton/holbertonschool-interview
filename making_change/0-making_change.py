#!usr/bin/env python3
"""Making change"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort()
    amount_of_coins = 0

    for i in range(len(coins) - 1, -1, -1):
        division = total // coins[i]
        if division > 0:
            amount_of_coins += division
            total = total - (division * coins[i])
        if total == 0:
            return amount_of_coins

    return -1
