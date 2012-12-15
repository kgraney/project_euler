#!/bin/env python
import csv

def gen_triangle_numbers():
	'''infinite generator for triangle numbers'''
	n = 1
	while True:
		yield 0.5*n*(n+1)
		n += 1

def letter_value(letter):
	'''a letter -> a value'''
	return ord(letter) - ord('a') + 1

def word_value(word):
	'''give the value of a word'''
	return sum((letter_value(l) for l in word.lower()))


# read single line of csv-style words
f = open('words.txt', 'r')
data = csv.reader(f).next()
f.close()

# map of unique word values and count of words with each value
values = {}
for v in [word_value(word) for word in data]:
	try:
		values[v] += 1
	except(KeyError): # first time seeing the value v
		values[v] = 1

# highest valued word (don't compute triangle numbers beyond here)
stop_value = max(values.keys())

# compute triangle numbers up to highest valued word, sum word counts
triangle_words = 0
for t in gen_triangle_numbers():
	try:
		triangle_words += values[t]	
	except(KeyError): pass # no words with this number
 
	if (t > stop_value):
		break

print(triangle_words)
