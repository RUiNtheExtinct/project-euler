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


def num(i, k):
    if k == 3:
        return (1 + mt.sqrt(1 + 12 * i * i - 4 * i)) // 2 == (
            1 + mt.sqrt(1 + 12 * i * i - 4 * i)
        ) / 2
    return (2 + mt.sqrt(4 + 48 * i * i - 16 * i)) // 8 == (
        2 + mt.sqrt(4 + 48 * i * i - 16 * i)
    ) / 8


# ! IF code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########

# for _ in range(uno()):
n, a, b = tres()
i = 1
j = (3 * i * i - i) // 2
while j < n:
    if num(i, a) == True:
        print(j)
    i += 1
    j = (3 * i * i - i) // 2


# ? Solution for Project Euler.
# n = uno()
# for i in range(286, n):
#     if (2 + mt.sqrt(4 + 16 * i * i + 16 * i)) // 8 == (
#         2 + mt.sqrt(4 + 16 * i * i + 16 * i)
#     ) / 8 and (1 + mt.sqrt(1 + 12 * i * i + 12 * i)) // 6 == (
#         1 + mt.sqrt(1 + 12 * i * i + 12 * i)
#     ) / 6:
#         print((i * i + i) // 2)
#         break


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
