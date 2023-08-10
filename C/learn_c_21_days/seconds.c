// Converts seconds (entered from users) to hours
#include <stdio.h>

#define SECS_PER_MIN 60 // define two constants
#define SECS_PER_HOUR 3600

unsigned seconds, minutes, hours, secs_left, mins_left; // definition of needed variables

int main(void) // creation of main method/function
{
    printf("Enter the number of seconds (< 65000): ");
    scanf("%d", &seconds);

    hours = seconds / SECS_PER_HOUR; // doing needed operations for conversion
    minutes = seconds / SECS_PER_MIN;
    mins_left = minutes % SECS_PER_MIN; // devides using the modulus operator (%) and
    secs_left = seconds % SECS_PER_MIN; // takes what's remaining from the division

    printf("%u seconds is equal to ", seconds); // printing the results
    printf("%u h, %u m, and %u s\n", hours, mins_left, secs_left);

    return 0;
}