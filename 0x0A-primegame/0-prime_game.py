#!/usr/bin/python3
"""
    a module containing a function isWinner which finds the winner in a game.
    - in a set of prime numbers that starts from 1 to n
    - a player remove a number and all it's multiples
    - the player who ends up having no moves becomes the looser
"""
def isWinner(x, nums):
    """
        - x is the number of rounds
        - nums is an array of n
        - returns the player with more wins or none if it can't be found
    """
    if x < 1 or not nums:
        return None
    maria_w, ben_w = 0, 0
    # generate a list posible primes numbers in the nums list
    n = max(nums)
    prime_list = [True for _ in range(1, n + 1, 1)]
    prime_list[0] = False
    for i, prime in enumerate(prime_list, 1):
        if i == 1 or not prime:
            continue
        for z in range(i + i, n + 1, i):
            prime_list[z - 1] = False
    # filter the number of primes less than n in nums per round
    for _, n in zip(range(x), nums):
        primes_len = len(list(filter(lambda x: x, prime_list[0: n])))
        ben_w += primes_len % 2 == 0
        maria_w += primes_len % 2 == 1
    if maria_w == ben_w:
        return None
    return 'Maria' if maria_w > ben_w else 'Ben'
