#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct 
{
    char name[31];
    char expire_date[8];
    long uid;
    double price;
    int amount_available;
} Medicine;

int main ()
{
    int n;

    FILE *fp;
    fopen("medicines.txt", "r");
    if (!fp)
    {
        printf("Unable to open file\n");
        exit(1);
    }
     
    Medicine *medicines;

    fread(n, sizeof(int), 1, fp);
    fread(medicines, sizeof(Medicine), n, fp);

    fclose(fp);
    return 0;
}

