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


# ! IF code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########

# for _ in range(uno()):
n, k = tres()
a = [0 for i in range(n + k + 1)]
for i in range(2, n + k + 1):
    if a[i] == 0:
        for j in range(i, n + k + 1, i):
            a[j] += 1
for i in range(n + 1):
    b = False
    for j in range(k):
        if a[i + j] != k:
            break
        if j == k - 1:
            b = True
    if b:
        print(i)
        break  # ? Comment this line for HackerRank Solution.


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
