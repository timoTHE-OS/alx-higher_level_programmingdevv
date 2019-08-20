#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    l = list_of_integers.copy()
    if l is None or l == []:
        return None
    if len(set(l)) == 1:
        return l[0]
    lo = 0
    hi = len(l)
    mid = ((hi - lo) / 2) + lo
    mid = int(mid)
    if hi == 2:
        return max(l)
    if l[mid] > l[mid - 1] and l[mid] > l[mid + 1]:
        return l[mid]
    if mid > 0 and l[mid] < l[mid + 1]:
        return find_peak(l[mid + 1:])
    if mid > 0 and l[mid] < l[mid - 1]:
        return find_peak(l[:mid])
