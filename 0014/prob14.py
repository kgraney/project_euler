#!/usr/bin/python

def next(n):
	if (n%2 == 0):
		return n/2
	else:
		return 3*n + 1

length_memo = {}

def sequence_length(n):

	num = n
	count = 1
	while (num != 1):
		if length_memo.has_key(num):
			length_memo[n] = count + length_memo[num] - 1
			return count + length_memo[num] - 1
		else:
			count = count + 1
			num = next(num)

	length_memo[n] = count
	return count


max_val = 0
max_length = 0
for i in reversed(range(1, 1000000)):
	length = sequence_length(i)
	if (length > max_length):
		max_val = i
		max_length = length
	if (i % 5000 == 0):
		print "checking   = " + str(i)

print "The longest chain is produced from " + str(max_val) + \
		" which has a length of " + str(max_length)
