#include <iostream>
#include <vector>

using namespace std;

int find_max(const vector<vector<int> > &triangle);
void print_triangle(const vector<vector<int> > &t);

int main(int argc, char* argv[])
{
	vector<vector<int> > t; // vector or rows

	//--------------------------------------------------------------------------
	// Read in the triangle from standard input
	int linenum = 1;
	while (1) {
		int m;
		vector<int> line;
		for (int i=0; i < linenum; i++) {
			cin >> m;
			if (cin.eof())
				goto doneread;
			line.push_back(m);
		}
		t.push_back(line);
		linenum++;
	};
doneread:

	// given t[i][j] in the maximum sequence, the next value can be either
	// t[i+1][j] or t[i+1][j+1]
	
	cout << find_max(t) << endl;

	return 0;
}

int find_max(const vector<vector<int> > &triangle)
{
	if (triangle.size() == 2) {
		return max(triangle[0][0] + triangle[1][0],
				triangle[0][0] + triangle[1][1]);
	} else {
		vector<vector<int> > left = triangle;
		vector<vector<int> >::iterator liter = left.begin();
		for (; liter != left.end(); liter++) {
			liter->pop_back();
		}
		left.erase(left.begin());

		vector<vector<int> > right = triangle;
		right.erase(right.begin());
		vector<vector<int> >::iterator riter = right.begin();
		for (; riter != right.end(); riter++) {
			riter->erase(riter->begin());
		}

		return max(triangle[0][0] + find_max(left),
				triangle[0][0] + find_max(right));

	}
}

void print_triangle(const vector<vector<int> > &t)
{
	vector<vector<int> >::const_iterator iter = t.begin();
	for (; iter != t.end(); iter++) {
		vector<int>::const_iterator iter2 = iter->begin();
		for (; iter2 != iter->end(); iter2++) {
			cout.width(2);
			cout << *iter2 << " ";
		}
		cout << endl;
	}
}
