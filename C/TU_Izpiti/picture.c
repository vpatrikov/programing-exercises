// ne sum podrejdal mn

#include <stdio.h>
#include <stdlib.h>

// zad 1
typedef struct
{
    int id;
    char artist_name[31];
    char painting_name[31];
    double price;
} Picture;

int main()
{
    int n;

    while (1)
    {
        printf("Enter n: ");
        scanf("%d", &n);

        if (n > 3 && n < 30)
        {
            break;
        }
        else
        {
            printf("Ivalid Input!\n");
        }
    }

    Picture *pictures;

    pictures = (Picture *)calloc(n * sizeof(Picture));

    if (!pictures)
    {
        printf("Unable to allocate memory\n");
        exit(1);
    }

    for (int i = 0; i < n; i++)
    {
        printf("Enter the id of the picture: ");
        scanf("%d", &pictures[i].id);

        printf("Enter the name of the artist: ");
        fgets(pictures[i].artist_name, sizeof(pctures[i].artist_name), stdin);
        pictures[i].artist_name[sizeof(pictures[i].artist_name) - 1] = '\0';

        printf("Enter the name of the painting: ");
        fgets(pictures[i].painting_name, sizeof(pctures[i].painting_name), stdin);
        pictures[i].painting_name[sizeof(pictures[i].painting_name) - 1] = '\0';

        printf("Enter the price of the painting: ");
        scanf("%lf", &pictures[i].price);
        getchar();
    }

    free(pictures);
    return 0;
}

// zad 2
double findMoreExpensivePics(Picture *pictures, int size, double price)
{
    int sum = 0;
    int count = 0;

    for (int i = 0; i < size; i++)
    {
        if (pictures[i].price > price)
        {
            sum += pictures[i].price;
            count++;
        }
    }

    if (count > 0)
    {
        return sum / count;
    }
    else
    {
        return 0;
    }
}

// zad 3
int writeToTxt(Picture *pictures, int size, char letter)
{
    FILE *fp;
    fp = fopen("info.txt", "w");

    if (!fp)
    {
        printf("Unable to open file\n");
        exit(3);
    }

    int count = 0;

    for (int i = 0; i < size; i++)
    {
        if (fprintf(fp, "%d; %s; %.2lf leva\n", pictures[i].id, pictures[i].painting_name, pictures[i].price) < 0)
        {
            printf("Unable to write picture #%d to file.\n", (i + 1));
        }
        else
        {
            count++;
        }
    }

    return count;
}