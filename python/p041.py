# import decimal as dec
import itertools as it

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


def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    i = 3
    while i * i < n:
        if n % i == 0:
            return False
        i += 2
    return True


def itup_to_int(t):
    t = t[::-1]
    ans, a = 0, 0
    for i in t:
        ans += i * (10 ** a)
        a += 1
    return ans


# ! If code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pr = []
for i in range(1, 10):
    for j in it.permutations(d[:i], i):
        k = itup_to_int(j)
        if is_prime(k) == True:
            pr.append(k)
pr.sort()
for _ in range(uno()):
    n = uno()
    ans = bi.bisect_left(pr, n) - 1
    if ans == -1:
        print(ans)
    else:
        print(pr[ans])


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
