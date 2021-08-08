# import decimal as dec
# import itertools as it
# import collections as coll
import sys
import math as mt

# import random as rd
# import bisect as bi
# import functions as ft
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


######## CODE STARTS FROM HERE ########
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for _ in range(uno()):
n = uno()
digits, ans = digits[:n], 0
print(digits)
d = {}


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
