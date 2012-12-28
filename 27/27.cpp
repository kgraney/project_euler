#include <iostream>
#include <set>

// slow recursive way to find primes, but that's OK, because we don't need many
// (also a cool example of C++11 compile-time metaprogramming, though it's not
// used here)
constexpr bool is_prime_recur(size_t num, size_t c)
{
	return (c*c > num) ? true : 
			(num % c == 0) ? false : is_prime_recur(num, c+1);
}

constexpr bool is_prime(size_t num)
{
	return (num <= 1) ? false : is_prime_recur(num, 2);
}

////////////////////////////////////////////////////////////////////////////////

int quadratic(int a, int b, int n)
{
	return n*n + a*n + b;
}

std::set<size_t> primes; // cache of prime numbers found so far

// highest known number below which cache contains all primes
size_t max_cached_prime = 2; 

bool is_prime_cache(int num)
{
	if (num <= 0) {
		// skip all the negative numbers
		return false;
	} else if (primes.find(num) != primes.end()) {
		// number is prime since it's in the cache
		return true;
	} else if (num < max_cached_prime) {
		// number should be cached if it's prime, so it's not
		return false;
	} else {
		// need to enlarge the cache before we know...	
		int i=max_cached_prime;
		for (; i <= num; i++) { // slow, but not use too much
			if (is_prime(i)) {
				primes.insert(i);
			}
		}
		max_cached_prime = i;
		return is_prime_cache(num);
	}
}


int main()
{
	int max_so_far = 0;
	for(int a=-999; a < 1000; a++) {
		for(int b=-999; b < 1000; b++) {
			int n = 0;
			for(; is_prime_cache(quadratic(a,b,n)); n++);
			if (n > max_so_far) {
				std::cout << a << ", " << b << ", " << n << std::endl;
				max_so_far = n;
			}
		}
	}
	std::cout << max_so_far << std::endl;
	return 0;
}

