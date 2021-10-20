# import decimal as dec
# import itertools as it
# import functools as ft
# import collections as coll
import sys
import math as mt
from pathlib import Path


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


# ! IF code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########


def is_triangular(n):
    m = (-1 + mt.sqrt(1 + 8 * 1 * n)) / 2
    if m == mt.floor(m):
        return int(m)
    return -1


for _ in range(uno()):
    print(is_triangular(uno()))


# ! Below code works for Project Euler only.
# f = open(r"../p042_words.txt", "r")
# words = f.read().split(",")
# ans = 0
# for i in range(len(words)):
#     words[i] = words[i].strip('"')
#     a = 0
#     for j in words[i]:
#         a += ord(j) - ord("A") + 1
#     if is_triangular(a) == True:
#         ans += 1
# print(ans)
# f.close()


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
