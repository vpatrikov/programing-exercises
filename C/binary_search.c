#include <stdio.h>
#include <stdlib.h>

int main()
{
    int size;
    printf("Enter the size of your array: ");
    scanf("%d", &size);

    int *array = (int *)malloc(size * sizeof(int));

    if (!array)
    {
        printf("Unable to allocate memory!");
    }
    
    for (int i = 0; i < size; i++)
    {
        array[i] = rand() % 999;
    }

    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - i - 1; j++)
        {
            if (array[j] > array[j + 1])
            {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }

    int low = 0;
    int high = size - 1;
    int target = array[5];

    while (low <= high)
    {
        int middle = low + (high - low) / 2;
        int value = array[middle];
        if (target > value)
        {
            low = middle + 1;
        }
        else if (target < value)
        {
            high = middle - 1;
        }
        else
        {
            printf("%d", middle);
            break;
        }
    }

    free(array);
}