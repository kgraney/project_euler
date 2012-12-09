#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{

	int a[] = {0,1,2,3,4,5,6,7,8,9};
	sort(a, a+10);

	for (unsigned int j=0; j < 999999; j++) {
		next_permutation(a,a+10);
	}

	for (int i=0; i < 10; i++)
		cout << a[i];
	cout << endl;

	return 0;
}
