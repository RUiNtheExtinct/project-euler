# from decimal import Decimal
import collections as coll
import sys
import math as mt

# import random as rd
# import bisect as bi
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


def div(n):
    i, ans = 2, 1
    while i * i <= n:
        if n % i == 0:
            ans += i
            if i != n // i:
                ans += n // i
        i += 1
    return ans


######## CODE STARTS FROM HERE ########
n = uno()
ans, d = 0, {}
for i in range(2, n):
    if i in d:
        continue
    p = div(i)
    q = div(p)
    d[i] = p
    d[p] = q
    if i == q and i != p:
        ans += i
        if p <= n:
            ans += p
print(ans)


# End Time
time2 = time.time()
print("Time Taken:", (time2 - time1) * 1000)
