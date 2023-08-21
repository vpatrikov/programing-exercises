#include <stdio.h>

float average(int sum, int count);
int a, b, c, d, e;
float f;

int main(void)
{
    puts("Enter five numbers:");
    scanf("%d%d%d%d%d", &a, &b, &c, &d, &e);

    int sum = a + b + c + d + e;

    f = average(sum, 5);

    printf("\nThe average of the five numbers is %f", f);

    return 0;
}

float average(int sum, int count)
{
    return (float)sum / count;
}