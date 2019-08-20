#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    if len(set(list_of_integers)) == 1:
        return list_of_integers[0]
    return find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak_helper(l, lo, hi):
    """Helper function using a Divide&Conquer algorithm
    to return a peak in a list of integers"""

    mid = ((hi - lo) / 2) + lo
    mid = int(mid)
    if mid > 0 and mid < len(l) - 1:
        if l[mid] > l[mid - 1] and l[mid] > l[mid + 1]:
            return l[mid]
    if mid == 0 and l[mid] > l[mid + 1]:
        return l[mid]
    if mid == len(l) - 1 and l[mid] > l[mid - 1]:
        return l[mid]
    if mid > 0 and l[mid] < l[mid + 1]:
        return find_peak_helper(l, mid + 1, hi)
    if mid > 0 and l[mid] < l[mid - 1]:
        return find_peak_helper(l, lo, mid - 1)
