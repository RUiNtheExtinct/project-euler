# import decimal as dec
# import itertools as it
# import functools as ft
# import collections as coll
import sys
import math as mt

# import random as rd
# import bisect as bi
# import functions as fn
import time

sys.setrecursionlimit(1000000)

# import numpy as np


def uno():
    return int(sys.stdin.readline().strip())


def dos():
    return sys.stdin.readline().strip()


def tres():
    return map(int, sys.stdin.readline().strip().split())


def cuatro():
    return sys.stdin.readline().strip().split()


# Starting Time
time1 = time.time()
mod = 1000000007


def is_pentagonal(m):
    if m < 1:
        return False
    n = (1 + mt.sqrt(1 + 24 * m)) / 6
    return n == mt.floor(n)


def pentagonal(n):
    return (n * (3 * n - 1)) // 2


# ! IF code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########

# for _ in range(uno()):
n, k = tres()
ans = []
for i in range(k + 1, n):
    p, q = pentagonal(i), pentagonal(i - k)
    if is_pentagonal(p + q) == True or is_pentagonal(p - q) == True:
        print(p)

# # ? Solution for project Euler.

# n = uno()
# ans = 10 ** 18
# for i in range(1, n + 1):
#     b = False
#     for j in range(i + 1, n + 1):
#         p, q = pentagonal(i), pentagonal(j)
#         if is_pentagonal(p + q) == True and is_pentagonal(q - p) == True:
#             ans = min(ans, q - p)
#             b = True
#             break
#     if b == True:
#         break
# print(ans)

# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
