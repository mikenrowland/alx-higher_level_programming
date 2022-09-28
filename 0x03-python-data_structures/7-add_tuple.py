#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = (0,0)
    tuple_a += c
    tuple_b += c 
    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return res
