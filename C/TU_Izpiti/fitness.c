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
    *members = realloc(*members, (*size) * sizeof(FitnessMember));

    printf("Enter first and last name: ");
    fgets((*members)[*size - 1].name, sizeof((*members)[*size - 1].name), stdin);
    (*members)[*size - 1].name[strcspn((*members)[*size - 1].name, "\n")] = '\0';

    printf("Enter the UID: ");
    fgets((*members)[*size - 1].uid, sizeof((*members)[*size - 1].uid), stdin);
    (*members)[*size - 1].uid[strcspn((*members)[*size - 1].uid, "\n")] = '\0';

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

    fprintf(fp, "%s; %s; %.2lf; %d\n", (*members)[*size - 1].name, (*members)[*size - 1].uid,
            (*members)[*size - 1].price, (*members)[*size - 1].locker_code);

    fclose(fp);
}

void printLessThanAvg(FitnessMember *members, int size)
{
    double sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += members[i].price;
    }
    double avg = sum / size;

    for (int i = 0; i < size; i++)
    {
        if (members[i].price < avg)
        {
            printf("%s - %s - %.2f\n", members[i].name, members[i].uid, members[i].price);
        }
    }
}

void printFromBinary(FitnessMember *members, char uid[7])
{
    FILE *fp;

    fp = fopen("members.bin", "rb");
    if (!fp)
    {
        printf("Unable to open file\n");
        exit(2);
    }

    char name[56];
    char id[7];
    double subscription_price;
    int locker_number;

    while (fread(name, sizeof(char), sizeof(name), fp)) {
        fread(id, sizeof(char), sizeof(id), fp);
        fread(&subscription_price, sizeof(double), 1, fp);
        fread(&locker_number, sizeof(int), 1, fp);

        if (strcmp(id, uid) == 0) {
            printf("Name: %s\n", name);
            printf("UID: %s\n", id);
            printf("Subscription price: %.2f\n", subscription_price);
            printf("Locker number: %d\n", locker_number);
        }
    }

    fclose(fp);
}

int main()
{
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    getchar();

    FitnessMember *members = (FitnessMember*)malloc(n * sizeof(FitnessMember));

    for (int i = 0; i < n; i++)
    {
        printf("Enter the names of the member: ");
        fgets(members[i].name, sizeof(members[i].name), stdin);
        members[i].name[strcspn(members[i].name, "\n")] = '\0';

        printf("Enter the UID: ");
        fgets(members[i].uid, sizeof(members[i].uid), stdin);
        members[i].uid[strcspn(members[i].uid, "\n")] = '\0';

        printf("Enter price: ");
        scanf("%lf", &members[i].price);

        printf("Enter the locker code/id: ");
        scanf("%d", &members[i].locker_code); 
        getchar();
    }   

    free(members);
    return 0;  
}
