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

// void reverse_string(string)
// {
//     char reverse_string[sizeof(string)]

//     for (int i = 0; i < length; i++)
//     {
//         reversedString[i] = inputString[length - 1 - i];
//     }
     // printf("%s", reverse_string);
// }

char* position(char alphabet)
{
    static char result[50]; // Static array to hold the result string
    int position = alphabet - 'a' + 1;

    // Format the string directly into the static array
    snprintf(result, sizeof(result), "Position of alphabet: %d", position);

    return result;
  }

unsigned mango(unsigned quantity, unsigned price)
{

    unsigned paidQuantity = quantity - quantity / 3;
    return paidQuantity * price;
}

int main(void)
{
    printf("%s", position('g'));
    return 0;
}