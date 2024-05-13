#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    char name[56];
    char uid[7];
    double price;
    int locker_code;
} FitnessMember;

void addMembers(FitnessMember **members, int *size)
{
    *size += 1;
    *members = (FitnessMember)realloc(*members, (*size) * sizeof(FitnessMember));

    printf("Enter first and last name: ");
    fgets((*members)[*size - 1].name, sizeof((*members)[*size - 1].name), stdin);
    (*members)[*size - 1].name[sizeof((*members).name) - 1] = '\0';

    printf("Enter the UID: ");
    fgets((*members)[*size - 1].uid, sizeof((*members)[*size - 1].uid), stdin);
    (*members)[*size - 1].uid[sizeof((*members).uid) - 1] = '\0';

    printf("Enter the price: ");
    scanf("%lf", &(*members)[*size - 1].price);

    printf("Enter the code of the locker: ");
    scanf("%d", &(*members)[*size - 1].locker_code);
    getchar();

    FILE *fp = fopen("membersText.txt", "a");

    if (!fp)
    {
        printf("Unable to create/open file!\n");
        exit(1);
    }

    fprintf(fp, "%d; %s; %s; %.2lf; %d\n", sizeof((*members)[*size - 1].name), (*members)[*size - 1].name, (*members)[*size - 1].uid,
            (*members)[*size - 1].price, (*members)[*size - 1].locker_code);

    fclose(fp);
}

int main()
{
    int n;
    printf("Enter the size of the array: ")
    scanf("%d", &n);
    getchar();

    FitnessMember *members = (FitnessMember*)malloc(n * sizeof(FitnessMember));

    for (int i = 0; i < n; i++)
    {
        printf("Enter the names of the member: ")
        fgets(members[i].name, sizeof(members[i].name), stdin);
    }   
    
    free(members);
    return 0;  
}
