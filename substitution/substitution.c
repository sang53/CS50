#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool letters(string key);
string convert(string text, string key);

int main(int argc, string argv[])
{
    string text;
    if(argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26 || !letters(argv[1]))
    {
        printf("Please enter 26 letters\n");
        return 1;
    }
    else
    {
        text = get_string("plaintext: ");
        text = convert(text, argv[1]);
        printf("ciphertext: %s\n", text);
        return 0;
    }
}

bool letters(string key)
{
    for(int i = 0; i < 26; i++)
    {
        key[i] = toupper(key[i]);
        if(key[i] < 65 || key[i] > 90)
        {
            return false;
        }
    }
    return true;
}

string convert(string text, string key)
{
    for(int i = 0; i < strlen(text); i++)
    {
        key[i] = toupper(key[i]);
        if(islower(text[i]))
        {
            text[i] = tolower(key[text[i] - 97]);
        }
        else if(isupper(text[i]))
        {
            text[i] = key[text[i] - 65];
        }
    }
    return text;
}