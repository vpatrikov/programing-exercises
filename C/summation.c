#include <stdio.h>

int summation(int num)
{
    int sum = 0;
    for (int i = 0; i < num + 1; i++)
    {
        sum += i;
    }

    return sum;
}

int main(void)
{
    int a = summation(1);
    printf("%d", a);
    return 0;
}