#include <stdio.h>

char get_grade(int a, int b, int c) {

    int score = (a+b+c)/3;
    if (90 >= score <= 100)
    {
        return 'A';
    }
    else if (80 >= score < 90)
    {
        return 'B';
    }
    else if (70 >= score < 80)
    {
        return 'C';
    }
    else if (60 >= score < 70)
    {
        return 'D';
    }
    else if (0 >= score < 60)
    {
        return 'F';
    }
    
}

int main (void)
{
    printf("%c", get_grade(10, 100, 50));
    return 0;
}