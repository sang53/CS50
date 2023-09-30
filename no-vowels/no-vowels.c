// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string text);

int main(int argc, string argv[])
{
    string answer;
    if(argc != 2)
    {
        printf("ERROR: enter an argument");
        return 1;
    }
    else
    {
        answer = replace(argv[1]);
    }
    printf("%s\n", answer);
}

string replace(string text)
{
    for(int i = 0; i < strlen(text); i++)
    {
        switch(text[i])
        {
            case 97:
                text[i] = 54;
                break;
            case 101:
                text[i] = 51;
                break;
            case 105:
                text[i] = 49;
                break;
            case 111:
                text[i] = 48;
                break;
        }
    }
    return text;
}