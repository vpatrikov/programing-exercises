#include <stdio.h>

int main()
{
    int a, b;
    printf("Enter height and width of rectangle: ");
    scanf("%d %d", &a, &b);
    
    for (int i = 1; i <= a; i++)
    {
        if (i == 1 || i == a)
        {
            for (int i = 0; i < b; i++)
            {
                printf("-");
            }
            
        }
        else
        {
            printf("-");
            for (int i = 0; i < b - 2; i++)
            {
                printf(" ");
            }
            printf("-");
        }
    printf("\n");
    }
}