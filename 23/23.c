#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

/* upper limit to compute towards */
const int UPPER_LIMIT = 28123;

int* abundants; /* array of abundant numbers */
int* proper_divisor_array; /* working space for divisor algorithm */
char* sieve; /* sieve of all candidate numbers */

/* print one of the above two arrays (for debugging) */
void print_array(int* array)
{
	int* p = array;
	while (*p) {
		printf("%d, ", *p);
		p = &p[1];
	}
	printf("\n");
}

/* return the sum of the proper divisor array */
int sum_proper_divisors()
{
	int sum = 0;
	int* p = proper_divisor_array;
	while (*p) {
		sum += *p;
		p = &p[1];
	}
	return sum;
}

/* populate the proper divisor array with proper divisors for the given
   number */
int* proper_divisors(int n)
{
	int* p = proper_divisor_array;
	for(int i=1; i <= sqrt(n); i++) {
		if (n % i == 0) {
			int j = n / i;
			p[0] = i;
			if (i != j && j != n) {
				p[1] = j;
				p = &p[2];
			} else {
				p = &p[1];
			}
		}
	}
}

void flag_sieve(int n)
{
	int* p = abundants;
	while (*p != 0) {
		sieve[*p + n] = 1;
		p = &p[1];
	}
}

int main()
{
	/* determine the max storage needed for the divisor list  (add one to
	   keep it zero-terminated) */
	int max_proper_divisors = ceil(sqrt(UPPER_LIMIT)) + 1;
	proper_divisor_array = malloc(max_proper_divisors*sizeof(int));

	/* size the abundant array with plenty of room, no need to get fancy */
	abundants = calloc(UPPER_LIMIT, sizeof(int));

	/* clear/allocate sieve space equal to the set of candidate numbers */
	sieve = calloc(UPPER_LIMIT+1, sizeof(char));

	/* compute all the abundant numbers, and for each one flag values in
	   the sieve that are the sum of that number and all previously
	   computed */
	int* p = abundants;
	for(int i=0; i <= UPPER_LIMIT; i++) {
		bzero(proper_divisor_array, max_proper_divisors*sizeof(int));
		proper_divisors(i);
		int sum = sum_proper_divisors();

		if (sum > i) { /* number is abundant, so store it */
			p[0] = i;
			p = &p[1];

			flag_sieve(i);
		}
	}

	/* sum all numbers from the sieve that aren't the sum of two abundant
	   numbers */
	int sum = 0;
	for(int i=0; i <= UPPER_LIMIT; i++) {
		if(sieve[i] == 0) {
			//printf("%d = %d\n", i, sieve[i]);
			sum += i;
		}
	}
	printf("%d\n", sum);

	return 0;
}
