#!/usr/bin/python3

from calculator_1 import sum, sub, mul, div
a = 10
b = 5
print("{} + {} = {}".format(a, b, sum(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
