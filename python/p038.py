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


def is_pandigital(s):
    return sorted(s) == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


# ! If code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########
# for _ in range(uno()):
n, r = tres()
ans = 123456789 // 10 ** (9 - r)
bounds = {2: 3, 3: 2, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for i in range(2, 10):
    for j in range(10 ** bounds[i], 10 ** (bounds[i] + 1)):
        a = ""
        for k in range(1, i + 1):
            a += str(k * j)
        if is_pandigital(a):
            ans = max(int(a), ans)
print(ans)

# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
