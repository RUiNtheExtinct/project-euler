# import decimal as dec
# import itertools as it
# import collections as coll
import sys
import math as mt

# import random as rd
# import bisect as bi
import functions as ft
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


######## CODE STARTS FROM HERE ########
r = uno()
a, ans, c = [0 for i in range(r + 1)], 0, [0]
j, b = 1, set()
while 2 ** j <= r:
    for k in range(2, r + 1):
        b.add(j * k)
    j += 1
    c.append(len(b))
# print(c)
for i in range(2, r + 1):
    if a[i] == 1:
        continue
    j = 1
    while i ** j <= r:
        a[i ** j] = 1
        j += 1
    ans += c[j - 1]

print(ans)

# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
