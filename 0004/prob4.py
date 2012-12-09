#!/usr/bin/python

# Returns true if a number is a palendrone
def is_palendrome(number):

	# Determine the maximum number of digits in the number
	pmax = 10;
	while (number / pmax != 0):
		pmax = pmax * 10;
	pmax /= 10;

	# Push each digit into the list
	digits = [];
	while (pmax > 0):
		one = number / pmax;
		number %= pmax;
		pmax /= 10;
		digits.append(one);

	# Compare digits
	while len(digits) > 1:
		if (digits.pop() != digits.pop(0)):
			return False;
	
	return True;


pals = [];
for i in range(100,1000):
	for j in range(100, 1000):
		n = i*j;
		if (is_palendrome(n)):
			pals.append(n);

print max(pals);
