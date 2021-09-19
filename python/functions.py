import decimal as dec
import itertools as it
import collections as coll
import sys
import math as mt

import random as rd
import bisect as bi

# import time

sys.setrecursionlimit(1000000)

import numpy as np


def uno():
    return int(sys.stdin.readline().strip())


def dos():
    return sys.stdin.readline().strip()


def tres():
    return map(int, sys.stdin.readline().strip().split())


def cuatro():
    return sys.stdin.readline().strip().split()


def powermod(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def eratosthenes_seive(n):
    size = n // 2
    sieve = [True] * size
    limit = int(n ** 0.5)
    for i in range(1, limit):
        if sieve[i]:
            val = 2 * i + 1
            tmp = ((size - 1) - i) // val
            sieve[i + val :: val] = [0] * tmp
    return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0]


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


def factorize(n):
    i = 1
    ct = 0
    while i * i < n:
        if n % i == 0:
            ct += 1
            if n // i != i:
                ct += 1
        i += 1
    return ct


def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0:
        return False
    i = 7
    while i * i < n:
        if n % i == 0:
            return False
        i += 2
    return True


def itup_to_int(t):
    t = t[::-1]
    ans, a = 0, 0
    for i in t:
        ans += i * (10 ** a)
        a += 1
    return ans


def isPal(s):
    return s == s[::-1]


def get_base_k(n, k):
    s = ""
    while n > 0:
        s += str(n % k)
        n //= k
    return s[::-1]


def char_to_ind(a):
    return ord(a) - ord("a")


def ind_to_char(i):
    return chr(i + ord("a"))


def num_width_base_10(n):
    return mt.floor(mt.log10(n)) + 1


def powers_in_range(n, r):
    return mt.floor(mt.log(r, n))


# Starting Time
# time1 = time.time()


# if __name__ == "__main__":
#     n = uno()
#     print(powermod(17, 41, 43))


# # End Time
# time2 = time.time()
# time = (
#     str(round((time2 - time1) * 1000, 3)) + "ms"
#     if (round((time2 - time1) * 1000, 3)) < 1000
#     else str(round(time2 - time1, 3)) + "s"
# )
# print("\nTime Taken:", time)
