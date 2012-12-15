#include <iostream>
#include <vector>

using namespace std;

vector<unsigned int> euclid(unsigned int m, unsigned int n);
unsigned int sum(vector<unsigned int> triple);

const int M_MAX = 100;
const int N_MAX = 100;

int main() {

	for (unsigned int n=1; n < N_MAX; n++) {
		for (unsigned int m=n+1; m < M_MAX; m++) {
			vector<unsigned int> triple = euclid(m,n);
			if (sum(triple) == 1000) {
				cout << triple[0] << " " << triple[1] << " " << triple[2] 
					<< endl;
				cout << "product = " << triple[0] * triple[1] * triple[2] 
					<< endl;
			}
		}
	}

	return 0;
}

// generate a pythagorean triple given two arbitrary integers
vector<unsigned int> euclid(unsigned int m, unsigned int n)
{
	vector<unsigned int> a;
	a.push_back(m*m - n*n);
	a.push_back(2*m*n);
	a.push_back(m*m + n*n);
	return a;
}

unsigned int sum(vector<unsigned int> triple)
{
	return triple[0] + triple[1] + triple[2];
}
