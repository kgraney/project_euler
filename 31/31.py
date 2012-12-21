#!/usr/bin/env python3

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

target = 200

# number of ways to obtain each value
counts = [1] + [0]*target

for v in coin_values:
	for u in range(v, target+1):
		counts[u] += counts[u-v]

print(counts[target])