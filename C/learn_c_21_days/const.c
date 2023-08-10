#include <stdio.h>

#define GRAMS_PER_POUND 454

const int TARGET_YEAR = 2023;

long weight_in_grams, weight_in_pounds;
int year_of_birth, age_in_2023;

int main(void)
{
    printf("Enter weight in pounds: ");
    scanf("%d", &weight_in_pounds);
    printf("Enter year of birth: ");
    scanf("%d", &year_of_birth);

    weight_in_grams = weight_in_pounds * GRAMS_PER_POUND;
    age_in_2023 = TARGET_YEAR - year_of_birth;

    printf("\nYour weight in grams = %ld", weight_in_grams);
    printf ("\nIn 2023 you wukk be %d years old\n", age_in_2023);

    return 0;
}