#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {

	int prev1 = 1, prev2 = 1;
	int next = 2;
	int sum = 0;
	for (int i=0; next < 4000000; i++) {
		if (next % 2 == 0)
			sum += next;

		//cout << next << endl;
		prev2 = prev1;
		prev1 = next;	

		next = prev1 + prev2;
	}

	cout << sum << endl;

	return 0;
}
