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
class Date(object):
    """A simple date abstraction representing a dd/mm/yyyy

    .. note:: the parameters are numbered in the natural way; i.e. ``day`` takes the range :math:`[1,31]`, ``month``
              takes the range :math:`[1,12]` and ``year`` takes the range :math:`[0, 9999]`.

    :param day: the initial date value (day, or dd)
    :param month: the initial date value (month, or mm)
    :param year: the initial date value (year, or yyyy)
    """

    def __init__(self, day: int, month: int, year: int):
        # Basic parameter validation
        assert isinstance(day, int), "day must be an integer"
        assert isinstance(month, int), "month must be an integer"
        assert isinstance(year, int), "year must be an integer"
        assert 1 <= day <= 31, "day must be in [1, 31]"
        assert 1 <= month <= 12, "month must be in [1, 12]"
        assert 0 <= year <= 9999, "year must be in [0, 9999]"

        # Store the initial date provided
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """ String representation of a Date object """
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def __le__(self, other: "Date") -> bool:
        """Test whether this ``Date`` instance is less than or equal to the `other` ``Date`` instance

        :param other: the ``Date`` instance to compare against
        :return: ``True`` if the current ``Date`` is equal to or before the `other` ``Date`` instance
        :return: ``False`` otherwise
        """

        if isinstance(other, Date):
            if self.year < other.year:
                return True  # earlier year
            elif self.year == other.year and self.month < other.month:
                return True  # same year, earlier month
            elif self.month == other.month and self.day < other.day:
                return True  # same year, same month, earlier day
        return False  # any other case

    def __add__(self, other: int) -> "Date":
        """Addition operator

        This class allows for integer values to be added to it. Semantically, this represents adding that integer number
        of days to the current date value stored. The new date value will be returned by this operator.

        :param other: the number of days to add to this ``Date`` instance
        :return: a new ``Date`` instance with `other` days added to the current value
        """

        if not isinstance(other, int):
            raise TypeError("unsupported operand type(s) for +")

        rv = Date(
            self.day, self.month, self.year
        )  # build new Date instance with the same value
        if rv.day + other > Date.days_to_a_month(rv.month, rv.year):
            other -= Date.days_to_a_month(rv.month, rv.year) - rv.day
            rv.day = 0
            rv.month += 1
        if rv.month > 12:
            rv.month = 1
            rv.year += 1
        rv.day += other
        return rv

    @staticmethod
    def leap_year(year: int) -> bool:
        """Test whether the given `year` is a leap-year

        :param year: the year to test
        :return: ``True`` if `year` is a leap-year, ``False`` otherwise
        """

        return ((year % 4) == 0) and (((year % 100) != 0) or ((year % 400) == 0))

    @staticmethod
    def days_to_a_month(month, year):
        """Compute the number of days in the month and year provided

        :param month: the given month
        :param year: the given year
        :return: the number of days in the given month and year
        """

        standard_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if month == 2 and Date.leap_year(year):
            return 29  # February has 29 days in a leap-year
        else:
            return standard_days[month - 1]


def solve():
    """ Compute the answer to Project Euler's problem #19 """

    lower_bound = Date(1, 1, 1901)
    upper_bound = Date(31, 12, 2000)
    current_date = Date(1, 1, 1900)
    answer = 0

    current_date += 6  # first Sunday after 1/1/1900

    # Skip over Sundays, one week at a time, until 1/1/1901
    while current_date <= lower_bound:
        current_date += 7  # next Sunday

    # Skip over Sundays, one week at a time, until 31/12/2000
    while current_date <= upper_bound:
        if current_date.day == 1:
            answer += 1  # this is a Sunday and the first of a month
        current_date += 7

    return answer


print(solve())

# End Time
time2 = time.time()
print("Time Taken:", (time2 - time1) * 1000)
