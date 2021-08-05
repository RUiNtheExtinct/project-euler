# import decimal as dec
# import itertools as it
# import collections as coll
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


def foo(n):
    return mt.floor(mt.log10(n)) + 1


######## CODE STARTS FROM HERE ########
n = uno()
i = 2
a, b, c = 1, 1, 1
while foo(c) < n:
    c = a + b
    b, a = c, b
    i += 1
print(i, c)


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)