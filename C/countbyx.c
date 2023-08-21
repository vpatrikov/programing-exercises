#include <stdio.h>

int main(void)
{
    int x, y;

    printf("Enter the value of x (start from and count by): ");
    scanf("%d", &x);
    printf("Enter the value of y (how many numbers): ");
    scanf("%d", &y);

    int count[y];

    for (int i = 0; i < y; i++)
    {
        count[i] = 0;
    }

    for (int i = 0; i < y; i++)
    {
        count[i] += x;
        printf(" %d", count[i]);
        x *= 2;
    }

    return 0;
}