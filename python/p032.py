# import decimal as dec
import itertools as it

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


# NOTE If code does't work on HackerRank refer the C++ code.
######## CODE STARTS FROM HERE ########
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for _ in range(uno()):
n = uno()
digits, ans = digits[:n], 0
d = {}
for i in it.permutations(digits, r=n):
    for j in range(1, n):
        for k in range(1, n - j):
            if n - j - k < j or n - j - k < k:
                break
            a, b, c = 0, 0, 0
            for t in range(j):
                a = a * 10 + i[t]
            for t in range(j, j + k):
                b = b * 10 + i[t]
            for t in range(j + k, n):
                c = c * 10 + i[t]
            if a * b == c:
                d[c] = 1
print(sum(d.keys()))


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
