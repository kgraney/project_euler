#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {

	int sos = 1;
	int sum = 1;
	int diff;

	for (int i=2; i <= 100; i++) {
		sos += i*i;
		sum += i;

		diff = sum*sum - sos;
		cout << i << "= " << diff << endl;
	}

	return 0;
}
