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


def factorize(n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    if n != 1:
        return False
    return True


def f(c):
    if c == 0:
        return 0
    return c // 10 ** mt.floor(mt.log10(c))


######## CODE STARTS FROM HERE ########
d = uno()
ans, mx = 0, 0
for i in range(3, d):
    if factorize(i):
        continue
    s, p, a = 0, 10, {}
    while True:
        q, r = p // i, p % i
        if (q, r) in a:
            # print(s - a[(q, r)], i)
            if s - a[(q, r)] > mx:
                mx, ans = s - a[(q, r)], i
            break
        a[(q, r)], s, p = s, s + 1, r * 10
print(ans)

# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
