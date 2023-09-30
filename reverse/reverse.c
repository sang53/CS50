#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        return 1;
    }

    // Read header
    WAVHEADER *header = calloc(1, sizeof(WAVHEADER));
    if (header == NULL)
    {
        return 1;
    }
    fread(header, 1, 44, input);

    // Use check_format to ensure WAV format
    if (!check_format(*header))
    {
        return 1;
    }

    // Open output file for writing
    FILE *output = fopen("output.wav", "w");
    if (output == NULL)
    {
        return 1;
    }

    // Write header to file
    fwrite(header, 1, 44, output);

    // Use get_block_size to calculate size of block
    const WORD blocksize = get_block_size(*header);
    free(header);

    // get new buffer
    int8_t *buffer = calloc(blocksize, sizeof(int8_t));

    // go to last sample of input
    fseek(input, -blocksize, SEEK_END);

    // Write reversed audio to file
    while (ftell(input) > 43)
    {
        fread(buffer, blocksize, 1, input);
        fwrite(buffer, blocksize, 1, output);
        fseek(input, 2 * -blocksize, SEEK_CUR);
    }

    free(buffer);
    fclose(input);
    fclose(output);
    return 0;
}

int check_format(WAVHEADER header)
{
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 1;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    WORD size = header.numChannels * header.bitsPerSample / 8;
    return size;
}