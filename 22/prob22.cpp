#include <iostream>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

unsigned int alphabetical_value(const string &name);

int main(int argc, char* argv[])
{
	list<string> names;

	string line;
	while (!cin.eof()) {
		getline(cin, line, ',');
		line.erase(0, 1); // leading quotation
		line.erase(line.end() - 1); // trailing quotation
		names.push_back(line);
	}

	names.sort();

	list<string>::iterator iter = names.begin();
	int pos = 1;
	unsigned long sum = 0;
	for (; iter != names.end(); iter++) {
		unsigned int val = alphabetical_value(*iter);
		sum += val * pos;
		pos++;
	}

	cout << sum << endl;

	return 0;
};


// return alphabetical value of a name
unsigned int alphabetical_value(const string &name)
{
	unsigned int value = 0;
	string::const_iterator iter = name.begin();
	for (; iter != name.end(); iter++) {
		value += (*iter - 'A' + 1);
	}

	return value;
}
