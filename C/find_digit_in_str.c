#include <stdio.h>
#include <ctype.h>

int get_number_from_string(const char *src)
{
    char *result;
    for (int i = 0; i < sizeof(src); i++)
    {
        if (isdigit(src[i]))
        {
            result[i] = src[i];
        }
    }
    return result;
}