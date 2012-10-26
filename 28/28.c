#include <stdio.h>

/* return the width of a given level's sides */
int side_width(int level)
{
	if (level == 1) {
		return 1;
	} else {
		return 2 + side_width(level - 1);
	}
}

/* return the total circumference of a level */
int level_size(int level)
{
	return 4*side_width(level) - 4;
}

/* return the highest numeric value for level */
int highest_val(int level)
{
	if (level == 1) {
		return 1;
	} else {
		return level_size(level) + highest_val(level - 1);
	}
}

/* return the sum of the corners for a level */
int corner_sum(int level)
{
	int delta = side_width(level) - 1; /* delta between corners */
	int i = highest_val(level - 1) + delta;
	int max = highest_val(level);
	int sum = 0;
	for (; i <= max; i+= delta) {
		sum += i;
	}
	return sum;
}


int main()
{
	/* Sides of spiral are 1001, so we want level_count such that 
	   1001 == side_width(level_count).  Turns out this value is
	   level_count == 501. */
	const int level_count = 501;

	int sum = 1; /* sum of the first level, loop starts at level 2 */
	for (int i=2; i <= level_count; i++) {
		sum += corner_sum(i);
		//printf("(LEVEL %d) cumulative sum = %d\n", i, sum);
		//printf("size = %d\n", side_width(i));
	}
	printf("sum of diagonals = %d\n", sum);
	return 0;
}
