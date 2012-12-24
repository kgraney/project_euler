#!/usr/bin/python3
import billionaire


f = 0.1
while f < 1.0:

	num_samples = 100

	ratio_sum = 0
	for i in range(0,num_samples):
		ratio = billionaire.run_trials(1e4, f)
		ratio_sum += ratio

	print(f, '%0.12f' % (ratio_sum/num_samples))

	f += 0.1	
