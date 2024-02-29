#!/usr/bin/python3
""" a module containing makeChange function that takes an array of
    coins available and the total amount needed as arguments"""


def makeChange(coins, total):
    """ a function that determine the fewest number of coins needed to
       meet a given amount total """
    if total <= 0:
        return 0

    current_total = 0
    total_coins_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        rmdr = (total - current_total) // coin
        current_total += rmdr * coin
        total_coins_used += rmdr
        if current_total == total:
            return total_coins_used
    return -1
