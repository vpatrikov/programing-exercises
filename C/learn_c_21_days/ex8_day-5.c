#include <stdio.h>
#include <string.h>

double devision(int a, int b);

int x, y;
double z;
char answer[3];

int main(void)
{
    do
    {
        puts("Input two numbers");
        scanf("%d%d", &x, &y);

        z = devision(x, y);

        printf("\n\n%.2f", z);

        printf("\nDo you want to go again?\n");
        scanf(" %s", &answer);
    } while (strcmp(answer, "yes") == 0);

    return 0;
}

double devision(int a, int b)
{
    if (b != 0)
    {
        return (double)a / b;
    }
    else
    {
        printf("\nYou cannot devide by zero!");
        return 0;
    }
}
