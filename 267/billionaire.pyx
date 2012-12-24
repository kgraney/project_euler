from cpython cimport bool

cdef extern from "stdlib.h": 
	long rand "rand"() 
	void srand "srand"(unsigned int seed) 
	int RAND_MAX "RAND_MAX"
cdef extern from "time.h": 
	ctypedef long time_t
	time_t time "time"(time_t* timer)

# threshold for 50% true bool
cdef int RAND_THRESHOLD = <int>(0.5 * (<double>RAND_MAX + 1.0))

srand(time(NULL))

cdef double goal = 1e9 # goal £1e9

# run a single sample of the game (1000 coin flips)
# return True if account is over £1e9 at conclusion
cdef bool bet1000(double f):
	cdef double account = 1 # start account at £1
	cdef unsigned int i
	for i in range(0, 1000):
		if rand() < RAND_THRESHOLD:
			account += 2*f*account
		else:
			account -= f*account

	return (account >= goal)


def run_trials(unsigned int num_trials, double f):
	cdef int num_passed = 0

	cdef int i
	for i in range(0,num_trials):
		if bet1000(f):
			num_passed += 1
			
	return num_passed / <double>num_trials
