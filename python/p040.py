# import decimal as dec
# import itertools as it
# import functools as ft
# import collections as coll
import sys
import math as mt

# import random as rd
import bisect as bi

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


def dign(n, i):
    return int(str(n)[i])


# ! If code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########
for _ in range(uno()):
    ans = 1
    arr = list(tres())
    dig = [0, 9]
    arr = [10 ** i for i in range(7)]
    for i in range(1, 25):
        dig.append(9 * (10 ** i) * (i + 1) + dig[i])
    for i in arr:
        m = bi.bisect_left(dig, i)
        mm = i - dig[m - 1]
        p, q = (
            10 ** (m - 1) + (mm - m) // m + (0 if (mm - m) % m == 0 else 1),
            mm % m if mm % m != 0 else m,
        )
        # print(mm, m, p, q, dign(p, q - 1))
        ans *= dign(p, q - 1)
        if ans == 0:
            break
    print(ans)

# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
