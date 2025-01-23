#include <stdio.h>
#include <stdlib.h>

void print_arr(int *arr, int size)
{
    printf("[ ");
    for (int i = 0; i < size; i++)
    {
        if (i != size - 1)
        {
            printf("%d, ", arr[i]);
        }
        else
        {
            printf("%d ]", arr[i]);
        }
    }
    printf("\n");
}

int main(void)
{
    int arr[] = {8, 3, 5, 6};
    int size = sizeof(arr) / sizeof(int);
    print_arr(arr, size);

    int end = size - 1; // cqlostniq razmer
    int index = 0;      // basically i in the for

    while (end > 0)
    {
        if (arr[index] > arr[index + 1])
        {
            int temp = arr[index]; // 109963sv
            arr[index] = arr[index + 1];
            arr[index + 1] = temp;
        }

        index++;

        if(index == end){ // kogato prikluchi dadenoto obhojdane
            end--; // premahvame sortiranata chast ot masiva
            index = 0; // prigotvqme index-a za sledvashtoto obhojdane
        }
    }

    print_arr(arr, size);
    return 0;
}
