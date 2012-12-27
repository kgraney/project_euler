#!/bin/env python3
from itertools import permutations

digits = range(0,10)
pandigitals = permutations(digits)

def l2d(l):
	return int(''.join(map(str, l)))

#pandigitals = [(1,4,0,6,3,5,7,2,8,9)]

total = 0
for n in pandigitals:
	if l2d(n[1:4]) % 2 == 0 and \
			l2d(n[2:5]) % 3 == 0 and \
			l2d(n[3:6]) % 5 == 0 and \
			l2d(n[4:7]) % 7 == 0 and \
			l2d(n[5:8]) % 11 == 0 and \
			l2d(n[6:9]) % 13 == 0 and \
			l2d(n[7:10]) % 17 == 0:
		print(n)
		total += l2d(n)

print(total)
