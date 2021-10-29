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


def isPal(s):
    return s == s[::-1]


def get_base_k(n, k):
    s = ""
    while n > 0:
        s += str(n % k)
        n //= k
    return s[::-1]


# NOTE If code doesn't work on HackerRank refer the C++ code if available.

######## NOTE CODE STARTS FROM HERE ########
# for _ in range(uno()):
n, k = tres()
ans = 0

for i in range(1, n):
    if isPal(str(i)) and isPal(get_base_k(i, k)):
        ans += i
print(ans)

# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
