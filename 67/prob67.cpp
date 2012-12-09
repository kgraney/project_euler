#include <iostream>
#include <vector>

using namespace std;

int find_max(vector<vector<int> > &triangle);
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

int find_max(vector<vector<int> > &triangle)
{
	for (int row = triangle.size() - 2; row >= 0; row--) {
		for (int i=0; i < triangle[row].size(); i++) {
			triangle[row][i] = max(triangle[row][i] + triangle[row+1][i],
						triangle[row][i] + triangle[row+1][i+1]);
		}
	}

	return triangle[0][0];
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
