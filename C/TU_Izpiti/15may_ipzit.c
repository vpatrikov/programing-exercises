#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char location[31];
    char leaving_date[11];
    double price;
    char uid[7];
    int length_days;
} Excursion;

int main()
{
 FILE *fp;
 fp= fopen("excursions.bin", "rb");

 if(!fp)
 {
    printf("Unable to open file");
    exit(1);
 }
 int n;
 fread(n, sizeof(int), 1, fp);

 Excursion *excursions;

 excursions = (Excursion*)malloc(n*sizeof(Excursion));

 if (!excursions)
 {
    printf("Unable to allocate memory.");
    exit(2);
 }

 fread(excursions, sizeof(Excursion), n, fp)
 

 fclose(fp);
 free(excursions);
 return 0;
}


void discountExcursion(Excursion *excursions, int size, int index)
{
    if (index > size - 1)
    {
        printf("Invalid Index");
        exit(3);
    }

    for (int i = 0; i < size; i++)
    {
        if (i == index)
        {
            excursions[i].price -= excursions[i].price * 0.03;
            printf("%.2lf лв. - %s - %s - %d дни\n", excursions[i].price, excursions[i].location, excursions[i].leaving_date, excursions[i].length_days);
        }  
    } 
}

int wrtiteToTxt(Excursion *excursions, int size, double min, double max)
{
    int count = 0;
    FILE *fp;

    fp = fopen ("excursionOffer.txt", "a");
    
    if (!fp)
    {
        printf("Unable to open/create file.\n");
        exit(4);
    }
    for (int i = 0; i < size; i++)
    {
        if (excursions[i].price > min && excursions[i].price < max)
        {
            fprintf(fp, "\n%s\n%s\n%d дена\n%.2lf лв.\n", excursions[i].location, excursions[i].leaving_date, excursions[i].length_days, excursions[i].price);
            count++;
        }
    }
    fclose(fp);
    return count;
}