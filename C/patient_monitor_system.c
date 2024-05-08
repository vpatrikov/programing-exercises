#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int procedure_id;
    char date[11];
    char procedure_name[31];
    char procedure_type[51];
} Procedure;

int count_procedures(Procedure* procedures, int size, char* patient_name, char* proc_type);
Procedure* add_new_procedure(Procedure* procedures, int size);
int write_procedure_report(Procedure* procedure, int size, char* proc_type);


int main()
{
    int n;
    FILE* fp;
    fread(n, sizeof(int), 1, fp)

    fp = fopen("procedures.bin", "rb");

    if (!fp)
    {
        printf("Unable to open file\n");
        exit(1);
    }

    Procedure* array;
    array = (Procedure*)malloc(n * sizeof(Procedure));

    fread(array, sizeof(Procedure), n, fp);
    
    fclose(fp);
    free(array);
    return 0;
}