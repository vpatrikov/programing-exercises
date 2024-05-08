#include <stdio.h>
#include <stdlib.h>

static int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int SortNumbersAscending(FILE* pinf) {
    int iRetVal = -1;
    int *numbers = NULL;
    int numElements = 0;

    // Move to the end of the stream in order to calculate the size
    fseek(pinf, 0, SEEK_END);
    // Get file size in bytes
    long int fileSize = ftell(pinf);
    
    // Calculate the number of elements we need to sort (excluding the first integer)
    if (fileSize > sizeof(int)) {
        numElements = (fileSize - sizeof(int)) / sizeof(int);
        numbers = (int*)malloc(numElements * sizeof(int));
        if (numbers == NULL) {
            // Memory allocation failed
            return -1;
        }
        
        // Move to the beginning of the numbers in the file
        fseek(pinf, sizeof(int), SEEK_SET);
        
        // Read numbers into the array
        fread(numbers, sizeof(int), numElements, pinf);

        // Sort the array
        qsort(numbers, numElements, sizeof(int), compare);

        // Create a new file to store the sorted numbers
        FILE *pfsorted = fopen("numbersBinSorted.bin", "w+b");
        if (pfsorted != NULL) {
            // Write the number of elements to the sorted file
            fwrite(&numElements, sizeof(int), 1, pfsorted);
            // Write the sorted numbers to the file
            fwrite(numbers, sizeof(int), numElements, pfsorted);
            fclose(pfsorted);
            iRetVal = 0;
        }
    }
    
    // Free dynamically allocated memory
    free(numbers);
    
    return iRetVal;
}

