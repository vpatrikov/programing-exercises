/* Tells the size of different C variable types in bytes */
#include <stdio.h>

int main (void)
{
    printf("\nThe size of the int type is %d bytes", sizeof(int));
    printf("\nThe size of the char type is %d bytes", sizeof(char));
    printf("\nThe size of the short type is %d bytes", sizeof(short));
    printf("\nThe size of the long type is %d bytes", sizeof(long));
    printf("\nThe size of the long long type is %d bytes", sizeof(long long));
    printf("\nThe size of the float is %d bytes", sizeof(float));


    return 0;
}