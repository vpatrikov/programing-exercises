#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    int id;
    char date[11];
    char name[31];
    char type[51];
} Procedure;

int count_procedures(Procedure *array, int size, char name[31], char type[51])
{
    int count = 0;

    for (int i = 0; i < size; i++)
    {
        if (array[i].name == name && array[i].type == type)
        {
            count++;
        }
    }

    return count;
}
Procedure *add_new_procedure(Procedure *array, int *size)
{
    Procedure new_p;
    printf("Enter name: ");
    fgets(new_p.name, sizeof(new_p), stdin);
    new_p.name[sizeof(new_p.name) - 1] = '\0';

    printf("Enter date (DD-MM-YYYY): ");
    fgets(new_p.date, sizeof(new_p.date), stdin);
    new_p.date[sizeof(new_p.date) - 1] = '\0';

    printf("Enter type:")
    fgets(new_p.type, sizeof(new_p.type), stdin);
    new_p.type[sizeof(new_p.type) - 1] = '\0';

    printf("Enter id: ");
    scanf("%d", &new_p.id);

    Procedure *newProcedures = realloc(array, (*n + 1) * sizeof(Procedure));
    newProcedures[*size] = new_p;
    (*size)++;
    return newProcedures;
}
int main()
{
    FILE *fp;
    fp = fopen("procedures.bin", "rb");

    if (fp == NULL)
    {
        printf("Unable to open file\n");
        exit(1);
    }

    int num_procedures;
    fread(num_procedures, sizeof(int), 1, fp);

    Procedure *procedures = (Procedure *)malloc(num_procedures * sizeof(Procedure));

    if (procedures == NULL)
    {
        printf("Unable to allocate memory.\n");
        exit(2);
    }

    fread(procedures, sizeof(Procedure), num_procedures, fp);


    free(procedures);
    fclose(fp);
    return 0;
}