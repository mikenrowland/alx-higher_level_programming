#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculate(args):
    if len(args) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if args[1] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(args[0])
    b = int(args[2])
    operator = args[1]

    if operator == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))

    if operator == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))

    if operator == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))

    if operator == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))


if __name__ == "__main__":
    calculate(sys.argv[1:])
