#include <stdio.h>


int sum_of_digits_squared(int n)
{
	int sum = 0;
	for (; n > 0; n /= 10) {
		int digit = n % 10;
		sum += digit * digit;
	}

	return sum;
}

int main()
{
	int limit = 10000000;

	int count = 0;
	for (int i=1; i < limit; i++) {
		int next = i;
		while (next != 89 && next != 1) {
			next = sum_of_digits_squared(next);
		}

		if (next == 89)
			count++;
	}

	printf("up to: %d, reach 89: %d\n", limit, count);
}
