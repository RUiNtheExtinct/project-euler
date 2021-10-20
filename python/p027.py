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


def sieve_for_primes_to(n):
    size = n // 2
    sieve = [True] * size
    limit = int(n ** 0.5)
    for i in range(1, limit):
        if sieve[i]:
            val = 2 * i + 1
            tmp = ((size - 1) - i) // val
            sieve[i + val :: val] = [0] * tmp
    return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0]


######## CODE STARTS FROM HERE ########
d = uno()
ans, mx = 0, 0
p, isp = sieve_for_primes_to(2000001), [False for i in range(5000001)]
for i in p:
    isp[i] = True
for a in range(-d + 1, d):
    for b in range(-d, d + 1):
        # print(a, b)
        n = 0
        while isp[n * n + a * n + b]:
            n += 1
        if n > mx:
            ans, mx = a * b, n
print(ans)


# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
