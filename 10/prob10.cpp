#include <iostream>
#include <vector>

using namespace std;

//const unsigned int MAX = 10;
const unsigned int MAX = 2000000;

int main(int argc, char *argv[])
{
	// populate the sieve with all values
	vector<unsigned int> sieve;
	sieve.reserve(MAX);
	for (unsigned int i = 2; i <= MAX; i++) {
		sieve.push_back(i);
	}



	// execute algorithm to strike out non-primes
	unsigned int p = 2;
	unsigned int newp = 0;
	while (p*p <= MAX) {
		//cout << "p = " << p << endl;
		vector<unsigned int>::iterator iter = sieve.begin();
		iter += p - 2 + p;
		for (; iter <= sieve.end(); iter += p) {
			//cout << "\t" << *iter << endl;
			*iter = 0;
		}

		// find new p
		iter = sieve.begin();
		iter += p - 1;
		while (*iter == 0) { iter++; }
		p = *iter;
	}



	// compute the sum
	vector<unsigned int>::iterator iter = sieve.begin();
	unsigned long long int sum = 0;
	for (; iter != sieve.end(); iter++) {
		if (*iter != 0) {
			//cout << *iter << " " << endl;
			sum += *iter;
		}
	}
	cout << sum << endl;

	return 0;
}
