#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char* string;
    printf("Enter a string: \n");

    string = (char*)malloc(100);

    if (string == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    int counter = 0;
    scanf("%s", string);

    for (int i = 0; string[i] != '\0'; i++)
    {
        counter++;
    }

    printf("%d\n", counter);

    free(string);

    return 0;
}
