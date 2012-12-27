#!/bin/env python3

def sum_fifths(n):
	return sum(int(d)**5 for d in str(n))


cum_sum = 0
for i in range(2,1000000):
	sum_fifth = sum_fifths(i)
	if i == sum_fifth:
		print(i)
		cum_sum += i

print('sum = %d' % cum_sum)
