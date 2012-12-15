#include <iostream>
#include <vector>
#include <math.h>
#include <set>

using namespace std;

typedef unsigned long long bigint;

set<bigint> find_divisors(bigint n);

int main(int argc, char *argv[])
{

	bigint counter = 1;
	bigint triangle = 1; // current triangle number
	set<bigint> divisors;

	while (1) {
		counter++;
		triangle += counter;

		divisors = find_divisors(triangle);
		if (divisors.size() >= 500) {
			cout << triangle;
			break;
		}
		divisors.clear();
	}

	return 0;
}

set<bigint> find_divisors(bigint n) {
	set<bigint> div;
	for (bigint i=1; i < sqrt(n); i++) {
		if (n % i == 0) {
			div.insert(i);
			div.insert(n/i);
		}
	}

	return div;
}
