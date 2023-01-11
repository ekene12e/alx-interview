#!/usr/bin/python3
"""
This function computes the fewest number 
of operations ( ctrl C, Ctrl V)
needed to reach a particular
number (n) of 'H' xters from a 
single xter"""


def minOperations(n):
    """
    A function that calculates the fewest number of operations
    needed to give a result of exactly n H characters in a file
    args: n: Number of characters to be displayed
    return:
          number of min operations
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
