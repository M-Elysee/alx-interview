#!/usr/bin/python3
""" a module containing a function minOperation """


def minOperations(n):
    """a method that calculates the fewest number of operations needed
       to result in exactly n H characters in the file."""
    if not isinstance(n, int):
        return 0
    op_num = 0
    store = 0
    t_chr = 1
    while t_chr < n:
        if store == 0:
            # initial copy all and paste
            store = t_chr
            t_chr += store
            op_num += 2
        elif (n - t_chr) % t_chr == 0:
            # copy all and paste
            store = t_chr
            t_chr += store
            op_num += 2
        elif store > 0:
            # only paste
            t_chr += store
            op_num += 1
    return op_num
