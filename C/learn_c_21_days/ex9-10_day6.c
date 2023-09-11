#include <stdio.h>

int main(void)
{
    int record = 0;
    while (record < 100)
    {
        printf( "\nRecord %d ", record);
        printf( "\nGetting next number..." );
        record++;
    }

    int counter;
    for (counter = 1; counter < 100; counter++)
        printf("\nCounter = %d", counter );
    return 0;
}