#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./license infile\n");
        return 1;
    }

    // Create buffer to read into
    char *buffer = malloc(sizeof(char) * 7);
    if (buffer == NULL)
    {
        return 2;
    }

    // Create array to store plate numbers
    char *plates[8];
    for (int i = 0; i < 8; i++)
    {
        plates[i] = malloc(sizeof(char) * 7);
    }

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 7, 1, infile) == 1)
    {
        // Replace '\n' with '\0'
        buffer[6] = '\0';

        // Save plate number in array
        strcpy(plates[idx], buffer);
        idx++;
    }

    for (int i = 0; i < 8; i++)
    {
        printf("%s\n", plates[i]);
    }
    free(buffer);
    for(int i = 0; i < 8; i++)
    {
        free(plates[i]);
    }
    fclose(infile);
}
