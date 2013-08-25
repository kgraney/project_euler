#include <iostream>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

string base = "123456789";

int test(string& str, int mult, int equal) {
		int op1 = atoi(str.substr(0, mult + 1).c_str());
		int op2 = atoi(str.substr(mult + 1, equal - mult).c_str());
		int prod = atoi(str.substr(equal + 1).c_str());

		if (op1 * op2 == prod) {
			cout << op1 << " " << op2 << " " << prod << endl;
			return prod;
		}

		return 0;
}

int main() {

	set<int> seen;
	int sum = 0;

	do {
		for (int i=0; i < base.size() - 1; i++) {
			for (int j=i + 1; j < base.size() - 1; j++) {
				int prod = test(base, i, j);
				if (prod != 0 && seen.find(prod) == seen.end()) {
					seen.insert(prod);
					sum += prod;
				}
			}
		}
	} while ( next_permutation(base.begin(), base.end()) );

	cout << "sum = " << sum << endl;
}

