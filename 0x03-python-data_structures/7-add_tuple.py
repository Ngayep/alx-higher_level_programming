#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) <= 1 or len(tuple_b) <= 1:
        new_tuple = (tuple_a[0] + tuple_b[0], 0)
    else:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
