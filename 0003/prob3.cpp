#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

typedef unsigned long long bigint;

struct node {
	bigint factor;
	struct node* left;
	struct node* right;

	node() : left(NULL), right(NULL) {}
};

bool split(struct node* np);
void recurse_split(struct node* root);

vector<bigint> pfs;

int main() {

	bigint num = 600851475143;
	bigint sq = sqrt(num);

	cout << "num  = " << num << endl;
	cout << "sqrt = " << sq << endl;
	
	struct node* root = new node;
	root->factor = num;

	recurse_split(root);

	bigint max = 0;
	for (vector<bigint>::iterator i = pfs.begin(); i != pfs.end(); i++) {
		if (*i > max)
			max = *i;
	}
	cout << max << endl;

	return 0;
}

void recurse_split(struct node* root) {
	if (root == NULL)
		return;
	
	if (split(root)) {
		recurse_split(root->left);
		recurse_split(root->right);
	} else {
		pfs.push_back(root->factor);
		return;
	}
}


// Splits a tree node into two of its primes and returns true, or returns false
// if the node cannot be split (the factor is prime).
bool split(struct node* np) {

	bigint s = sqrt(np->factor);
	struct node* node1 = new node;
	struct node* node2 = new node;


	for (bigint i=2; i < s; i++) {
		if (np->factor % i == 0) {
			np->left = node1;
			np->right = node2;

			node1->factor = np->factor / i;
			node2->factor = np->factor / node1->factor;
			return true;	
		}
	}

	return false;
}
