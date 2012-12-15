#!/usr/bin/python
from math import sqrt;

def is_prime(number):
	for i in range(2, 1 + int(sqrt(number))):
		if (number % i == 0):
			return False
	return True

i = 0
num = 1
while (i < 10001): 
	num += 1
	if(is_prime(num)):
		i += 1

print num
