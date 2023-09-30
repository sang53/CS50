#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    float L = (float) letters / words * 100.0;
    float S = (float) sentences / words * 100.0;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int index1;
    if ((int) (index * 10) % 10 < 5)
    {
        index1 = index;
    }
    else
    {
        index1 = index + 1;
    }
    if (index1 < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index1 > 15)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index1);
    }
}

int count_letters(string text)
{
    int n = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] > 64 && text[i] < 91) || (text[i] > 96 && text[i] < 123))
        {
            n++;
        }
    }
    return n;
}

int count_words(string text)
{
    int n = 0;
    for (int i = 0; i < strlen(text) - 1; i++)
    {
        if (text[i + 1] == 32 && text[i] != 32)
        {
            n++;
        }
    }
    if (text[strlen(text) - 1] != 32)
    {
        n++;
    }
    return n;
}

int count_sentences(string text)
{
    int n = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 63 || text[i] == 46 || text[i] == 33)
        {
            n++;
        }
    }
    return n;
}