#!/usr/bin/python3
import sys

def add(args):
    sum = 0
    for i in args:
        if i == args[0]:
            continue
        sum += int(i)
    print(sum)

if __name__ == "__main__":
    add(sys.argv)
