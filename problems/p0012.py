#!/usr/bin/env python3
# coding: utf-8


"""
Highly Divisible Triangular Number

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle
number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
        1: 1
        3: 1,3
        6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28
 
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""


PID = 12
ANSWER = 76576500

TIMEOUT_EXT = 2000


def get_divisors(n: int) -> int:
    """
    Get the number of divisors of n.
    """
    c, i = 2, 2
    while i * i <= n:
        if n % i == 0:
            c += 2
        i += 1

    return c


def solve() -> int:
    n, i = 1, 2
    while get_divisors(n) < 500:
        n += i
        i += 1

    return n
