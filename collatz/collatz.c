#include <cs50.h>
#include <stdio.h>

int collatz(int n);

int main(void)
{
    int n = get_int("Type in the number: ");
    int answer = collatz(n);
    printf("It will take %i times\n", answer);
}

int collatz(int n)
{
    if (n == 1)
    {
        return 0;
    }
    else if (n % 2 == 0)
    {
        return collatz(n / 2) + 1;
    }
    else
    {
        return collatz(3 * n + 1) + 1;
    }
}