/* ++a adds 1 to the variable on the line that it's called while
    a++ adds 1 to the given variable after the execution of the line on which
    it's written */
#include <stdio.h>
#include <stdlib.h> // used for the system("cls") which cleans the console

// ! These defines could be useful in the future

void selection();
int add_to_int(int a);
long factorial(int x);

int main(void)
{
    selection();
    return 0;
}

int add_to_int(int a)
{
    int b = a++; // adds one after the execution of this line

    // ! same as "if (b> a) int z = b; else int z = a;"
    printf("The larger value is %d", (b > a) ? b : a); // ? saves space and looks cleaner
    return 0;
}

// * To calculate a factorial you have to take a variable, multiply it by itself and multiply it by the factorial of the variable - 1
// ! Here's an example

long factorial(int x)
{
    if (x == 0 || x == 1)
    {
        return 1;
    }
    else
    {
        return x * factorial(x - 1);
    }
}

void selection()
{
    int choice;
        printf("Enter the number of the function you want to execute: \n");

        printf("Enter the number of the function you want to execute:\n");
        printf("1. add_to_int\n");
        printf("2. factorial\n");
        scanf("%d", &choice);

        system("cls");

        switch (choice)
        {
        case 1:
        {
            printf("Enter a value for a: ");
            int a;
            scanf("%d", &a);
            add_to_int(a);
            break;
        }
        case 2:
        {
            int y;
            printf("Enter a value for y: ");
            scanf("%d", &y);
            long z = factorial(y);
            printf("The value of the factorial of y is = %ld\n", z);
            break;
        }
        default:
            printf("Invalid choice.\n");
            break;
        }
}
