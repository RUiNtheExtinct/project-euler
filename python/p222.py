def best(r, n):
    ans = 0
    for j in range(n - 1):
        p = r[j] + r[j + 1]
        ans += mt.sqrt(p * p - (100 - p) * (100 - p))
    return ans + r[0] + r[-1]


import math as mt
import itertools

t = [49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
p = [i for i in range(30, 50, 2)]
print(p)

n = len(t)
print(best(t, n))