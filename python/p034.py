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


def fac(n, fact):
    ans = 0
    while n > 0:
        ans += fact[n % 10]
        n //= 10
    return ans


# NOTE If code doesn't work on HackerRank refer the C++ code if available.

######## NOTE CODE STARTS FROM HERE ########
# for _ in range(uno()):
n = uno()
fact, ans, lim = [1] * 10, 0, 1
for i in range(1, 10):
    fact[i] = fact[i - 1] * i
# print(fact)
while lim * fact[9] >= int(lim * "9"):
    # print(lim)
    lim += 1
lim = int((lim - 1) * "9")
for i in range(3, lim + 1):
    if fac(i, fact) == i:
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
