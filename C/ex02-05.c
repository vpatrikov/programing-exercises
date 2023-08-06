// counts characters and spaces in input
#include <stdio.h>
#include <string.h>
int main (void){
    char buffer[256];

    printf ("Enter your name and press <Enter>:\n");
    gets(buffer);

    printf ("Your name has %d charecters and spaces!", strlen(buffer));

    return 0;
}