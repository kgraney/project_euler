#!c:\Python33\python.exe
import math

factorial = []
for i in range(0,10):
	factorial.append(math.factorial(i))

cache = {}
hit = 0
total = 0

# begin at 3 to avoid 1! and 2!, which don't count
for num in range(10,100000):
	digits = tuple(int(d) for d in str(num))
	
	try_part = digits[1:]
	if (try_part in cache):
		hit += 1
		factorial_sum = cache[try_part] + factorial[digits[0]]
	else:
		factorial_sum = sum(factorial[d] for d in digits)
	
	total += 1
	cache[digits] = factorial_sum

	if (num == factorial_sum):
		print(num)

print('cache hits: %d/%d' % (hit, total))