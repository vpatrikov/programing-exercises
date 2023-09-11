// TODO: Count by from 1 to 100 by 3s with different statements

#include <stdio.h>

int main(void)
{
    int i = 1;
    // ? Done with a for statement
    printf("\n");
    for (; i <= 100; i += 3)
    {
        printf("%d ", i);
    }
    printf("\n");

    // ? Done with a while statement
    i = 1;
    while (i <= 100)
    {
        printf("%d ", i);
        i += 3;
    }

    // ? Done with a do...while statement
    i = 1;
    do
    {
        printf("%d ", i);
        i += 3;
    } while (i <= 100);

    return 0;
}