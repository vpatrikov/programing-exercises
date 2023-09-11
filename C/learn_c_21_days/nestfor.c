#include <stdio.h>

void draw_box (int, int);

int main (void)
{
    draw_box(4, 8);

    return 0;
}

void draw_box (int row, int column)
{
    int col;
    for (; row > 0; row--)
    {
        for (col = column; col > 0; col--)
            printf("X");

        printf("\n");
    }
}
