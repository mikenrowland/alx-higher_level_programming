#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list)
    y = x - 1
    for _ in range(x):
        print("{:d}".format(my_list[y - x]))
        y = y - 1
