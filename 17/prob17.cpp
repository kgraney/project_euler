#include <iostream>
#include <vector>
#include <string>

using namespace std;

const string BASES[] = {
	"", "one", "two", "three", "four", "five", "six", "seven", "eight",
	"nine" };

const string TEENS[] = {
	"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
	"seventeen", "eighteen", "nineteen" };

const string TENS[] = {
	"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
	"ninety" };

void add_count(const string &s, int &count) {
	count += s.length();
	//static int c = 0;
	//c++;
	//cout << c << "\t" << s << "\t" << s.length() << endl;
}

int main()
{
	int length = 0;
	vector<string> base_hundred;

	// 1-9
	for (int i=1; i < 10; i++) {
		base_hundred.push_back(BASES[i]);
		add_count(BASES[i], length);
	}

	// 10-19
	for (int i=0; i < 10; i++) {
		base_hundred.push_back(TEENS[i]);
		add_count(TEENS[i], length);
	}

	// 20-99
	for (int i=0; i < 8; i++) {
		for (int j=0; j < 10; j++) {
			base_hundred.push_back(TENS[i] + BASES[j]);
			add_count(TENS[i] + BASES[j], length);
		}
	}

	// 100-999
	for (int i=1; i < 10; i++) {
		add_count(BASES[i] + "hundred", length);
		vector<string>::iterator iter = base_hundred.begin();
		for (; iter != base_hundred.end(); iter++) {
			add_count(BASES[i] + "hundredand" + *iter, length);
		}
	}

	// 1000
	add_count("onethousand", length);

	cout << length << endl;
	return 0;
}
