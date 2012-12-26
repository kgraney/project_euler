#!/usr/bin/python
from IPython.parallel import Client
import numpy 

rc = Client()
dview = rc[:]

@dview.parallel(block=True)
def try_fs(lst):
	import billionaire
	result = []
	for f in lst:
		num_samples = 10

		ratio_sum = 0
		for i in range(0,num_samples):
			ratio = billionaire.run_trials(1e4, f)
			ratio_sum += ratio

		result.append((f, (ratio_sum/num_samples)))

	return result


#dview.block = True
#dview.execute('import billionaire')
#s = dview.map_sync(lambda x: billionaire.run_trials(1e4, x), f_samples)

f_samples = numpy.arange(0.208, 0.210, 0.0001)
print(f_samples)
samples = try_fs(f_samples)
for s in samples:
	print(s)

