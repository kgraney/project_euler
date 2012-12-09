#!/usr/bin/python
from math import factorial

value = factorial(100)

sum = 0
while (value != 0):
	sum = sum + (value % 10)
	value = value / 10

print sum
