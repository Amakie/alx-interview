#!/usr/bin/python3
"""change making problem"""


def makeChange(coins, total):
    """function that returns the fewest number of coins"""
    if total < 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for t in range(1, total + 1):
        for coin in coins:
            if coin > t:
                pass
            elif t - coin >= 0:
                dp[t] = min(dp[t], 1 + dp[t - coin])

    return dp[total] if dp[total] != total + 1 else -1
