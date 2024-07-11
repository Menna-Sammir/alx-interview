#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H '''
    if n <= 0:
        return 0

    min_ops = float('inf')

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            min_ops = min(min_ops, i + n // i)

    return min_ops
