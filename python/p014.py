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


def collartz(g, n):
    while n != 1:
        if n in g:
            return
        if n & 1:
            g[n] = 3 * n + 1
            n = 3 * n + 1
        else:
            g[n] = n // 2
            n = n // 2


######## CODE STARTS FROM HERE ########
mx, ans, g, n = 0, 0, {}, int(input())
p = {}
for i in range(2, n):
    collartz(g, i)
for i in g:
    a, b = 0, i
    while g[b] != 1:
        if b in p:
            a += p[b]
            break
        b = g[b]
        a += 1
    p[i] = a
    if a > mx:
        mx = a
        ans = i
print(ans)


# End Time
time2 = time.time()
print("Time Taken:", (time2 - time1) * 1000)
