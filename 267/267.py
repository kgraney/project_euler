#!/usr/local/bin/python3
from random import getrandbits

class Account(object):
	def __init__(self, initial_value, f):
		self.value = initial_value
		self.f = f

	def bet1000(self):
		for i in range(0,1000):
			self.bet()

	def bet(self):
		won = getrandbits(1)

		if (won):
			self.value += 2*self.f*self.value
		else:
			self.value -= self.f*self.value

	def __str__(self):
		return 'Value: $%0.4f' % (self.value)


class Trial(object):
	def __init__(self, f):
		self.f = f
		self.trial_size = 10000

	def run_trial(self):
		passes = 0
		for i in range(0, self.trial_size):
			account = Account(1, self.f)
			account.bet1000()
			if (account.value > 1e9):
				passes += 1

		ratio = passes/self.trial_size
		print('passed %d of %d (%f)' % (passes, self.trial_size, ratio))
		return ratio


t = Trial(1/4)
t.run_trial()

#a = Account(1, 1/2)
#print(a)
#a.bet1000()
#print(a)
