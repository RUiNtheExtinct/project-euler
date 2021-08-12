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


# ! IF code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########


prime = nloglogn_seive(500005)
for _ in range(uno()):
    n = uno()
    ans = 0
    for j in range(1, mt.ceil(mt.sqrt(n / 2))):
        # print(i, j, i - 2 * j * j)
        if prime[n - 2 * j * j] == True:
            ans += 1
    print(ans)


# ? Solution for Project Euler.
# n = uno()
# prime = nloglogn_seive(n)
# # print(prime[57])
# for i in range(35, n, 2):
#     if prime[i] == True:
#         continue
#     b = False
#     for j in range(1, mt.ceil(mt.sqrt(i / 2))):
#         # print(i, j, i - 2 * j * j)
#         if prime[i - 2 * j * j] == True:
#             b = True
#             break
#     if b == False:
#         print(i)
#         break


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
