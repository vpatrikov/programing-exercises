// TODO: Rewrite Listing 5.4 so that it needs only one return statement in the larger_of() function

#include <stdio.h>

int x, y, z;

int larger_of(int a, int b);

int main (void)
{
    puts("Enter two values:");
    scanf("%d%d", &x, &y);
    z = larger_of(x, y);
    printf("\nThe larger value is %d", z);
    return 0;
}

int larger_of(int a, int b)
{
    return (a > b) ? a : b;
}