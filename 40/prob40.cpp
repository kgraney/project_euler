#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void add_number(string &s, unsigned int n);

int main()
{
	string f;
	for (unsigned int i=1; i < 200000; i++)
		add_number(f, i);

	int prod = 1;
	for (unsigned int i=1; i <= 1000000; i *= 10)
		prod *= (f[i - 1] - '0');
	cout << prod << endl;

	return 0;
}

void add_number(string &s, unsigned int n)
{
	stringstream ss;
	ss << n;
	s.append(ss.str());
}
