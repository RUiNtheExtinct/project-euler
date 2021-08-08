# import decimal as dec
# import itertools as it
# import collections as coll
import sys

# import math as mt

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


######## CODE STARTS FROM HERE ########
dp = [[0 for i in range(100001)] for j in range(9)]
for i in range(9):
    dp[i][0] = 1
w = [1, 2, 5, 10, 20, 50, 100, 200]
tr = []

for _ in range(uno()):
    r = uno()
    
    tr.append(r)
    for i in range(1, 9):
        for j in range(1, r + 1):
            if w[i - 1] <= j:
                dp[i][j] = dp[i][j - w[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[8][r] % 1000000007)

# End Time
time2 = time.time()
time = (
    str(round((time2 - time1) * 1000, 3)) + "ms"
    if (round((time2 - time1) * 1000, 3)) < 1000
    else str(round(time2 - time1, 3)) + "s"
)
print("\nTime Taken:", time)
