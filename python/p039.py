# import decimal as dec
# import itertools as it
# import functools as ft
import collections as coll
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


# ! If code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########
mx = 5000001
d, d1, bb = coll.defaultdict(lambda: 0), list(), 0
for i in range(1, mt.ceil(mt.sqrt(mx)) // 2):
    for j in range(1, i):
        if i % 2 == 1 and j % 2 == 1:
            continue
        if mt.gcd(i, j) > 1:
            continue
        k = 1
        while True:
            a = k * (i * i - j * j)
            b = k * 2 * i * j
            c = k * (i * i + j * j)
            k += 1
            if a + b + c > mx:
                break
            d[a + b + c] += 1
d1.append(0)
for i in d:
    if bb < d[i]:
        bb = d[i]
        d1.append(i)

# print(d[60])

for _ in range(uno()):
    n = uno()
    ans = 12
    l = len(d1)
    print(d1[bi.bisect_right(d1, n, lo=0, hi=l) - 1])


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
