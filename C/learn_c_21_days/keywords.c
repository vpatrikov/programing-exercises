#include <stdio.h>

int squared(int x);

int main(void) {
    typedef int cqlo_chislo;
    cqlo_chislo a, c;

    printf("Enter a value for a: ");
    scanf("%d", &a);

    c = squared(a);
    printf("The square of %d is %d\n", a, c);

    return 0;
}

int squared(int x) {
    return (x * x);
}
