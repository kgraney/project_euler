#!/bin/env python3

def is_palindrone(n):
	s = str(n)
	return s == s[::-1]

def is_binary_palindrone(n):
	s = bin(n)[2:]
	return s == s[::-1]

s = 0
for i in range(0,1000000):
	if is_palindrone(i) and is_binary_palindrone(i):
		s += i

print(s)
