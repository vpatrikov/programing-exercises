#include <stdio.h>
#include <math.h>

#define MAX 100

int digPow(int n, int p)
{
    int n_copy = n;
    int arr[MAX];
    int i = 0;

    while (n_copy > 0)
    {
        int r = n_copy % 10;
        arr[i] = r;
        i++;
        n_copy = n_copy / 10;
    }

    int sum = 0;

    for (int j = 0; j < i; j++)
    {
        sum += pow(arr[j], p);
        p++;
    }

    int result = sum / n;
    if (result == 1)
    {
        return result;
    }
    else
    {
        return -1;
    }
}

int main(void)
{
    printf("%d\n", digPow(89, 1));
    return 0;
}
