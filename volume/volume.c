// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    uint8_t *temp8 = malloc(sizeof(uint8_t) * HEADER_SIZE);
    if (temp8 == NULL)
    {
        return 1;
    }
    for (int i = 0; i < HEADER_SIZE; i++)
    {
        fread(temp8, HEADER_SIZE, 1, input);
        fwrite(temp8, HEADER_SIZE, 1, output);
    }

    // free memory
    free(temp8);

    // TODO: Read samples from input file and write updated data to output file
    int16_t *temp16 = malloc(sizeof(uint16_t));
    if (temp16 == NULL)
    {
        return 1;
    }
    while (fread(temp16, 2, 1, input))
    {
        *temp16 = *temp16 * factor;
        fwrite(temp16, 2, 1, output);
    }

    // free memory
    free(temp16);
    // Close files
    fclose(input);
    fclose(output);
}
