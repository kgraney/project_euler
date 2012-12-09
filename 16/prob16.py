#!/usr/bin/python

value = 2**1000
#value = 2**15

sum = 0
while (value != 0):
	sum = sum + (value % 10)
	value = value / 10

print sum
