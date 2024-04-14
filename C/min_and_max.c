#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n;
    printf("Enter the size of your array: ");
    scanf("%d", &n);

    if (n <= 0)
    {
        printf("Invalid Size");
    }
    

    int *array = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        while (1)
        {
            if (!scanf("%d", &array[i]))
            {
                while (getchar() != '\n');
                printf("Input is not an integer!\n");
            }
            else
            {
                break;
            }
        }
    }

    int min = array[0];
    int max = array[0];

    for (int i = 1; i < n; i++)
    {
        if (array[i] > max)
        {
            max = array[i];
        }
        else if (array[i] < min)
        {
            min = array[i];
        }
        
           
    }
    printf("The largest number in the array is: %d\n", max);
    printf("The smallest number in the array is: %d\n", min);
    return 0;
}