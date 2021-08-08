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


def nloglogn_seive(n):
    lp = [0] * (n + 1)
    prime = [True] * (n + 1)
    pr = []
    prime[0] = prime[1] = False
    for i in range(2, n):
        if prime[i] == True:
            lp[i] = i
            pr.append(i)
        j = 0
        while j < len(pr) and pr[j] <= lp[i] and i * pr[j] < n:
            prime[i * pr[j]] = False
            lp[i * pr[j]] = pr[j]
            j += 1
    return prime


def circp(n, prime):
    s = 2 * str(n)
    t = len(str(n))
    for i in range(t):
        if prime[int(s[i : t + i])] == False:
            return False

    return True


# NOTE If code doesn't work on HackerRank refer the C++ code if available.

######## NOTE CODE STARTS FROM HERE ########
# for _ in range(uno()):
n = uno()
prime, ans = nloglogn_seive(n + 5), 0
# s = set()
for i in range(2, n):
    if circp(i, prime) == True:
        ans += 1
        # s.add(i)
# print(sorted(s))
# print(e)
print(ans)

# print()


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
