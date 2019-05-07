#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 >= 2 and len2 >= 2:
        new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    elif len1 == 1 and len2 == 2:
        new_tuple = tuple_a[0] + tuple_b[0], tuple_b[1]
    elif len1 == 2 and len2 == 1:
        new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1]
    elif len1 == 1 and len2 == 1:
        new_tuple = tuple_a[0] + tuple_b[0]
    elif len1 == 2 and len2 == 0:
        new_tuple = tuple_a
    elif len1 == 0 and len2 == 2:
        new_tuple = tuple_b
    elif len1 == 1 and len2 == 0:
        new_tuple = tuple_a[0]
    elif len1 == 0 and len2 == 1:
        new_tuple = tuple_b[0]
    elif len1 == 0 and len2 == 0:
        new_tuple = ()

    return new_tuple
