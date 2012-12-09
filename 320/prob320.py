#!/usr/bin/python

fact_memo = {}
def fact(n):
	if n == 1:
		return 1
	elif fact_memo.has_key(n-1):
		result = n * fact_memo[n-1]
	else:
		result = n * fact(n-1)
	fact_memo[n] = result
	return result

def n(i):
	div = fact(i) ** 1234567890
	print "div = " + str(div)


def s(u):
	result = 0
	for i in range(10,u+1):
		result = result + n(i)
	return result

s(1)
#print s(1000)
