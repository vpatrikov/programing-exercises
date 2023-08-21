#include <stdio.h>

int product(int a, int b);

int x, y, z;

int main(void)
{
    puts("Enter two numbers: ");
    scanf("%d%d", &x, &y);

    z = product(x, y);

    printf("The product of those two numbers is equal to %d", z);
}

int product (int a, int b)
{
    return a * b;
}