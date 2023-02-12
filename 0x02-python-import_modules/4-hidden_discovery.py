#!/usr/bin/python3
import hidden_4


def print_hidden():
    for item in dir(hidden_4):
        if item[:2] != '__':
            print(item)


if __name__ == "__main__":
   print_hidden()
