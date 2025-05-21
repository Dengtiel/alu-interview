#!/usr/bin/python3
"""
Module to determine the minimum number of operations
to achieve exactly n H characters.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations
    (Copy All and Paste) to get n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations needed,
        or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations