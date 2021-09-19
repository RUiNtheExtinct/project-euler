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


# ! IF code doesn't work on HackerRank refer the C++ code if available.

######## ? CODE STARTS FROM HERE ########


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


def stup_to_int(t):
    a = 0
    for i in t:
        a = a * 10 + int(i)
    return a


# for _ in range(uno()):
n, k = tres()
sieve = nloglogn_seive(n * 5)
for i in range(1001, n):
    if sieve[i]:
        a = {}
        for j in it.permutations(str(i)):
            b = stup_to_int(j)
            if sieve[b]:
                a[b] = 1
        if len(a) < k:
            continue
        a.pop(i)
        b = str(i)
        ii = i
        for _ in a:
            if (_ + ii) // 2 in a:
                b += str((_ + ii) // 2) + str(_)
                ii = 2 * _ - (_ + ii) // 2
                break
        if k == 4 and ii in a:
            b += str(ii)
        if len(b) > len(str(i)):
            print(b)


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
