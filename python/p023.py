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
ans, up, d = 0, 28123, set()
# print(d)
for i in range(1, up):
    if div(i) > i:
        d.add(i)
    if not any((i - j in d) for j in d):
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