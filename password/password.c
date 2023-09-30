// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool uletter, lletter, number, symbol = false;
    for (int i = 0; i < strlen(password); i++)
    {
        if (password[i] > 64 && password[i] < 91)
        {
            uletter = true;
        }
        else if (password[i] > 96 && password[i] < 123)
        {
            lletter = true;
        }
        else if (password[i] < 48 && password[i] > 32)
        {
            symbol = true;
        }
        else if (password[i] > 47 && password[i] < 58)
        {
            number = true;
        }
    }
    if (uletter && lletter && number && symbol)
        {
            return true;
        }
    else
    {
        return false;
    }
}
