/*
 * This program outputs a list of each digit with digits that must come before
 * that digit and those that must come after.  The final answer can be easily
 * deduced from this output.
 */
#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<list>
#include<map>

using namespace std;

template<typename T> void eliminateDuplicates(vector<T>& v);
vector<int> explodeDigits(int n);
list<pair<int, int> > createPairs(const vector<vector<int> >& attempts);
map<int,list<int> > generateAfterMap(const list<pair<int,int> >& pairs);
map<int,list<int> > generateBeforeMap(const list<pair<int,int> >& afterMap);

void printPairs(const list<pair<int, int> >& pairs);
void printMaps(map<int,list<int> > beforeMap, 
		map<int,list<int> > afterMap);

int main(int argc, char* argv[])
{
	//>> Read in numbers from file
	vector<int> numbers;
	
	ifstream keylog("keylog.txt");
	if ( !keylog.is_open() ) {
		cerr << "Error opening keylog.txt file!" << endl;
		exit(1);
	}

	while (!keylog.eof()) {
		int n;
		keylog >> n;
		numbers.push_back(n);
	}

	//>> Eliminate duplicate numbers
	eliminateDuplicates(numbers);

	vector<vector<int> > digits;
	digits.reserve(numbers.size());
	vector<int>::iterator iter = numbers.begin();
	for (; iter != numbers.end(); iter++) {
		digits.push_back(explodeDigits(*iter));
	}

	//>> Generate list of pair constraints
	list<pair<int,int> > constraints = createPairs(digits);

	//>> Print lists of before and after constraints
	//printPairs(constraints);
	map<int,list<int> > afterMap = generateAfterMap(constraints);
	map<int,list<int> > beforeMap = generateBeforeMap(constraints);
	printMaps(beforeMap, afterMap);
	cout << endl;

}

// Eliminates duplicates from a vector
template<typename T>
void eliminateDuplicates(vector<T>& v)
{
	sort(v.begin(), v.end());
	v.erase(unique(v.begin(), v.end()), v.end());
}

// Explodes an integer into a vector of its digits
vector<int> explodeDigits(int n)
{
	stringstream ss;
	ss << n;
	string s = ss.str();
	vector<int> digits;
	for (int i=0; i < s.length(); i++) {
		digits.push_back(s[i] - '0');
	}
	return digits;
}

// Creates a list of pair constraints such that the first number must come
// before the second number.
list<pair<int, int> > createPairs(const vector<vector<int> > &attempts)
{
	list<pair<int, int> > pairs;

	vector<vector<int> >::const_iterator attempt = attempts.begin();
	for (; attempt != attempts.end(); attempt++) {
		vector<int>::const_iterator digit1 = attempt->begin();
		for (; digit1 < attempt->end(); digit1++) {
			vector<int>::const_iterator digit2 = digit1 + 1;
			for (; digit2 < attempt->end(); digit2++) {
				pair<int,int> p;
				p.first = *digit1;
				p.second = *digit2;
				pairs.push_back(p);
			}
		}
	}

	return pairs;
}

// Prints the pair constraints
void printPairs(const list<pair<int, int> > &pairs)
{
	cout << pairs.size() << " pair constraints" << endl;
	list<pair<int, int> >::const_iterator i = pairs.begin();
	for (; i != pairs.end(); i++) {
		cout << "\t" << i->first << " " << i->second << endl;
	}
}

// Generates a map of a digit to digits required after the digit
map<int,list<int> > generateAfterMap(const list<pair<int,int> >& pairs)
{
	map<int,list<int> > afterMap;
	list<pair<int, int> >::const_iterator i = pairs.begin();
	for (; i != pairs.end(); i++) {
		afterMap[i->first].push_back(i->second);
	}

	map<int,list<int> >::iterator iter = afterMap.begin();
	for (; iter != afterMap.end(); iter++) {
		// eliminate duplicates
		iter->second.sort();
		iter->second.erase(unique(iter->second.begin(), iter->second.end()),
				iter->second.end());
	}

	return afterMap;
}

map<int,list<int> > generateBeforeMap(const list<pair<int,int> >& pairs)
{
	map<int,list<int> > beforeMap;
	list<pair<int, int> >::const_iterator i = pairs.begin();
	for (; i != pairs.end(); i++) {
		beforeMap[i->second].push_back(i->first);
	}

	map<int,list<int> >::iterator iter = beforeMap.begin();
	for (; iter != beforeMap.end(); iter++) {
		// eliminate duplicates
		iter->second.sort();
		iter->second.erase(unique(iter->second.begin(), iter->second.end()),
				iter->second.end());
	}
	return beforeMap;
}

void printMaps(map<int,list<int> > beforeMap, 
		map<int,list<int> > afterMap)
{
	for (int i=0; i < 10; i++) {
		// before map list
		list<int>::const_iterator beforeiter = beforeMap[i].begin();
		for (; beforeiter != beforeMap[i].end(); beforeiter++) {
			cout << *beforeiter << " ";
		}

		cout << " ---->" << i << "<---- ";

		// after map list
		list<int>::const_iterator afteriter = afterMap[i].begin();
		for (; afteriter != afterMap[i].end(); afteriter++) {
			cout << *afteriter << " ";
		}
		cout << endl;
	}
}
