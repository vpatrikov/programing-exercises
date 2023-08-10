/* ++a adds 1 to the variable on the line that it's called while
    a++ adds 1 to the given variable after the execution of the line on which
    it's written */
#include <stdio.h>

int main(void)
{
    int a = 2;
    int b = a++; // adds one after the execution of this line

                                    // ! same as "if (b> a) int z = b; else int z = a;" 
    printf("The larger value is %d", (b > a) ? b : a); // ? saves space and looks cleaner
    return 0;
}