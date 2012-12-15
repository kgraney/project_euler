#!/usr/bin/python

def dl(n,m):
	digits = [int(i) for i in str(n*m)]
	digits.sort()
	return digits

def check_digits(n):
	return dl(n,2) == dl(n,3) == dl(n,4) == dl(n,5) == dl(n,6)

n = 1
while (check_digits(n) == False):
	n = n + 1

print n
