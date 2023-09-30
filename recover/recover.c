#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void advancecount(char count[8]);
bool testforheader(uint8_t *buffer);

int main(int argc, char *argv[])
{
    // check for 1 image, abort if not
    if (argc != 2)
    {
        printf("Usage: ./recover card.raw\n");
        return 1;
    }

    // open file
    FILE *image = fopen(argv[1], "r");
    if (image == NULL)
    {
        printf("File could not be found.\n");
        return 1;
    }

    // allocate memory for placeholder reader bytes (4 bytes)
    uint8_t *buffer = calloc(512, sizeof(uint8_t));
    if (buffer == NULL)
    {
        printf("Not enough memory\n");
        return 2;
    }

    // string to store jpg file name
    char currentcount[8] = "000.jpg";

    // get pointer for new jpg files
    FILE *jpg = fopen(currentcount, "w");
    if (jpg == NULL)
    {
        return 2;
    }

    // initial loop to remove dead space at the start
    do
    {
        fread(buffer, 1, 512, image);
    }
    while (!testforheader(buffer));
    fwrite(buffer, 1, 512, jpg);

    // loop until EOF
    while (fread(buffer, 1, 512, image) == 512)
    {
        // test if buffer == header
        if (testforheader(buffer))
        {
            // close current output, advance count & create new jpg
            fclose(jpg);
            advancecount(currentcount);
            jpg = fopen(currentcount, "w");
        }

        // write buffer into output file
        fwrite(buffer, 1, 512, jpg);
    }

    // free allocated memory
    free(buffer);
    fclose(image);
    fclose(jpg);
}

bool testforheader(uint8_t *buffer)
{
    if (*buffer == 0xff)
    {
        if (buffer[1] == 0xd8)
        {
            if (buffer[2] == 0xff)
            {
                if (buffer[3] < 0xef && buffer[3] > 0xdf)
                {
                    return true;
                }
            }
        }
    }
    return false;
}

void advancecount(char count[8])
{
    // advance unit place
    count[2]++;

    // check if above 9
    if (count[2] == 58)
    {
        // advance tens place & reset units = 0
        count[1]++;
        count[2] = '0';

        // test hundreds place
        if (count[1] == 58)
        {
            // advance hundreds & reset tens = 0
            count[0]++;
            count[1] = '0';
        }
    }
}