#include <stdio.h>

int radius, area;

int find_area (void) // calculates the area of a circle
{
	printf ("Enter radius: ");
	scanf ("%d", &radius);
	area = (int) (3.14159 * radius * radius);
	printf("\n\nArea = %d\n", area);
	return 0;
}

int x, y;

int print_x (void) // prints the letter 'X' 10 times in row and columns
{
	for (x = 0; x < 10; x++, printf("\n"))
		for (y = 0; y<10; y++)
			printf("%c", 1);
	return 0;
}

int bugged_method (void)
{
	printf("This is a program with a ");
	return 0;
}

int main (void)
{
	print_x();
}
