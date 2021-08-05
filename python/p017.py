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


######## CODE STARTS FROM HERE ########
def number_to_english(n):

    ones = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        None,
        None,
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n <= 90 and n % 10 == 0:
        return tens[n // 10]
    elif 20 < n < 100:
        return tens[n // 10] + "-" + ones[n % 10]
    elif 100 <= n <= 900 and n % 100 == 0:
        return ones[n // 100] + " hundred"
    elif 100 < n < 1000:
        return ones[n // 100] + " hundred and " + number_to_english(n % 100)
    elif 1000 < n < 10000:
        pass
    elif n == 1000:
        return "one thousand"
    else:
        raise ValueError("unexpected input")


def solve():
    """ Compute the answer to Project Euler's problem #17 """
    target = 1000
    answer = 0
    for i in range(target):
        words = number_to_english(i + 1).replace(" ", "").replace("-", "")
        answer += len(words)
    print(answer)


solve()
# End Time
time2 = time.time()
print("Time Taken:", (time2 - time1) * 1000)
