#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int (*test1)[3] = calloc(4, sizeof(int));
    int (*test2)[4] = calloc(3, sizeof(int));

    if (test1 == NULL || test2 == NULL)
    {
        return 1;
    }
    int count = 1;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            test1[i][j] = count;
            test2[i][j] = count;
            printf("1: %i\n2: %i\nc: %i\n", test1[i][j], test2[i][j], count);
            count++;
        }
    }

    free(test1);
    free(test2);
}