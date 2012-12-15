#!/usr/bin/python

fib_memo = {}
def fib(n):
	if n == 1 or n == 2:
		return 1

	key1 = fib_memo.has_key(n-1)
	key2 = fib_memo.has_key(n-2)
	if key1 and key2:
		result = fib_memo[n-1] + fib_memo[n-2]
	elif key1:
		result = fib_memo[n-1] + fib(n-2)
	elif key2:
		result = fib(n-1) + fib_memo[n-2]
	else:
		result = fib(n-1) + fib(n-2)

	fib_memo[n]	= result
	return result

num = 0
i = 0
while (num / 10**999 == 0):
	i = i + 1
	num = fib(i)

print i
