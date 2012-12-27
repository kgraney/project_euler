#!/bin/env python3

MAX = 100

s = set()
for a in range(2,MAX+1):
	for b in range(2,MAX+1):
		s.add(a**b)

print(len(s))
