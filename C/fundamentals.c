#include <stdio.h>
#include <ctype.h>

int twice_as_old(int father_age, int son_age)
{
    int twice_as_old = father_age - 2 * son_age;

    if (twice_as_old < 0)
    {
        return twice_as_old * -1;
    }
    else
    {
        return twice_as_old;
    }
}

int factorial(int number)
{
    int a = 0;
    printf("Enter a number: ");
    scanf("%d", &a);

    int prod = 1;
    for (int i = 1; i < (a + 1); i++)
    {
        prod *= i;
    }
    // printf("%d\n", prod);
    return prod;
}

void reverse_string(string)
{
    char reverse_string[sizeof(string)]

    for (int i = 0; i < length; i++)
    {
        reversedString[i] = inputString[length - 1 - i];
    }
    printf("%s", reverse_string);
}
int main(void)
{
    factorial(5);
    reverse_string("Hello World");
    return 0;
}