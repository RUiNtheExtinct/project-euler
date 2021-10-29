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


def itup_to_int(t):
    t = t[::-1]
    ans, a = 0, 0
    for i in t:
        ans += i * (10 ** a)
        a += 1
    return ans


# ! IF code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########

# for _ in range(uno()):
n = uno()
a, b, ans = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 5, 7, 11, 13, 17], 0
a = a[: n + 1]
# print(a)
for i in it.permutations(a, n + 1):
    # if i[0] == 0:
    #     continue
    c = True
    for j in range(1, n - 1):
        d = i[j] * 100 + i[j + 1] * 10 + i[j + 2]
        if d % b[j] != 0:
            c = False
            break
        # print(d)
    if c == True:
        # print(i)
        ans += itup_to_int(i)
print(ans)


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
