#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = (0,0)
    if len(tuple_a) == 1:
        tuple_a += c
    if len(tuple_b) <= 1:
        tuple_b += c 
    res = tuple(map(sum, zip(tuple_a, tuple_b)))
    return res
