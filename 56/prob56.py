#!/usr/bin/python

def sum_digits(n):
	return reduce(lambda x,y: x+y, [int(i) for i in str(n)])

mval = 0
for a in range(1,101):
	for b in range(1,101):
		val = sum_digits(a**b);
		if (val > mval):
			mval = val
print mval
