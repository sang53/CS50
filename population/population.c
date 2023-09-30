#include <cs50.h>
#include <stdio.h>

int calculate(int start, int end);

int main(void)
{
    // Prompt for start size
    int startpop = get_int("What is the starting population?\n");
    while (startpop < 9)
    {
        startpop = get_int("Please enter a number 9 or larger\n");
    }
    // Prompt for end size
    int endpop = get_int("What is the ending population? \n");
    while (endpop < startpop)
    {
        endpop = get_int("Please enter a number larger or equal to the starting population of %i\n", startpop);
    }

    // Calculate number of years until we reach threshold
    int nyears = calculate(startpop, endpop);

    // Print number of years
    printf("Years: %i", nyears);
}

int calculate(int start, int end)
{
    int current = start;
    int deaths;
    int births;
    int counter = 0;
    while (current < end)
    {
        deaths = current / 4;
        births = current / 3;
        current = current - deaths + births;
        counter++;
    }

    return counter;
}