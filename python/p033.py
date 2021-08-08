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


# NOTE If code doesn't work on HackerRank refer the C++ code.

######## NOTE CODE STARTS FROM HERE ########
# for _ in range(uno()):
n, k = tres()
ans, ans1, ans2 = 1, 0, 0
for den in range(10 ** (n - 1) + 1, 10 ** n):
    for num in range(10 ** (n - 1), den):
        if mt.gcd(num, den) % (10 ** (n - 1)) == 0:
            continue
        a = mt.gcd(num, den)
        if a == 1:
            continue
        p, q, r, s, t = str(num), str(den), "", "", 0
        kk = k
        for i in range(n):
            if p[i] in q:
                t += 1
        if t < k:
            continue


print(ans1, ans2)

# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
