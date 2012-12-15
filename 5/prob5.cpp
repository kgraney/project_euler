#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {

	// find 1*2*3*...*19*20
	unsigned long long max = 1;
	for (int i=2; i <= 20; i++)
		max = max * i;


	cout << "max = " << max << endl;
	bool flagged = false;
	for (unsigned long long i=20; i < max; i += 20) {
		for (int j=3; j <= 20; j++) {
			if (i%j != 0) {
				goto failed_test;
			}
		}

		cout << "FOUND! i=" << i << endl;
		return 0;

		failed_test:
		asm("nop");
	}



	cout << "END OF RANGE REACHED" << endl;

	return 0;
}
