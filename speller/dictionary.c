// Implements a dictionary's functionality

#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 500000;
//#define LENGTH 45

// Hash table
node *table[N];

unsigned int numwords = 0, maxhash = 0, minhash = 0;
void storeword(node *n, char *word);
void ridof(node *n2);
bool checkword(node n3, const char *word);
void checksize(node n4);

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // get hash value for word
    unsigned int hashn = hash(word);

    // check if it exists in table
    return checkword((*table)[hashn], word);
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // prime numbers for calcuation
    int lprimes[] = {149, 5, 11, 73, 17, 23, 31, 37, 197, 47, 257, 59, 83, 167, 103, 113, 131, 79, 137, 239, 157, 181, 227, 233, 211, 97};
    int pprimes[] = {293, 101, 199, 33, 151, 283, 127, 53, 191, 271, 71, 223, 11, 41, 173, 251, 163, 29, 139, 89, 19};

    // temporary storage variables
    unsigned int hashn = 0;
    char letter;
    int vowels = 0, cs = 0;

    // loop for every letter
    for (int i = 0; i < 20; i++)
    {
        // if end of string, break and return hash
        if (word[i] == '\0')
        {
            break;
        }

        // make letter lower and increase hash by position & value
        letter = tolower(word[i]);
        switch (letter)
        {
            case 39:
                hashn -= 1;
                break;
            default:
                hashn += (lprimes[letter - 97] * pprimes[i]);
                cs++;
                break;
        }
    }
    return hashn;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // variables & memory for dictionary & table
    FILE *dict = fopen(dictionary, "r");
    *table = calloc(N, sizeof(node));
    char *l = malloc(sizeof(char) * (LENGTH + 1));

    // check if valid memory allocation
    if (*table == NULL)
    {
        printf("NO SPACE\n");
    }
    if (dict == NULL)
    {
        return false;
    }
    if (l == NULL)
    {
        return false;
    }

    // counter for wordlength
    int count = 0;
    int totalwords = 0;

    // loop to read word, 1 letter at a time
    while (fread(l + count, 1, 1, dict))
    {
        // if end of word
        if (l[count] == '\n')
        {
            // change \n to \0 to mark end of string
            totalwords++;
            l[count] = '\0';

            // generate a hash number for word
            unsigned int hashn = hash(l);

            // store max & min hash numbers for faster searching
            if (hashn > maxhash)
            {
                maxhash = hashn;
            }
            else if (hashn < minhash)
            {
                minhash = hashn;
            }

            // store word into appropriate table
            storeword(&(*table)[hashn], l);

            // reset counter for next word
            count = 0;
        }
        else
        {
            // increment counter for next letter
            count++;
        }
    }

    // free allocated memory
    free(l);
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // loop for every array in table
    for (int i = minhash; i < maxhash + 1; i++)
    {
        // if there is a first letter add to count
        if ((*table)[i].word[0] != 0)
        {
            numwords++;
        }
        // if there is a valid pointer
        if ((*table)[i].next != NULL)
        {
            // check the connecting node
            checksize(*(*table)[i].next);
        }
    }
    return numwords;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // loop for every array used
    for (int i = minhash; i < maxhash + 1; i++)
    {
        // free allocated array starting at 1 node deep
        ridof((*table)[i].next);
    }

    // free rest of table
    free(*table);
    return true;
}

// function to store words recursively
void storeword(node *n, char *word)
{
    // if currently not used
    if (n->word[0] == 0)
    {
        // store word into node
        int i = 0;
        do
        {
            n->word[i] = tolower(word[i]);
            i++;
        }
        while (word[i] != '\0');
    }
    // if used but no next node
    else if (n->next == NULL)
    {
        // make a new node
        node *n1 = calloc(1, sizeof(node));
        if (n1 == NULL)
        {
            printf("NO");
            return;
        }

        // set current node pointer to next node
        n->next = n1;

        // store word in new node
        storeword(n->next, word);
    }
    // if used and pointer exists
    else
    {
        // recurse to see if node connecting to it has a pointer
        storeword(n->next, word);
    }
    return;
}

// function to free memory recursively
void ridof(node *n2)
{
    // if node doesn't exist just return
    if (n2 == NULL)
    {
        return;
    }
    // if there is a valid pointer
    else if (n2->next != NULL)
    {
        // remove the connecting node recursively
        ridof(n2->next);
    }
    // free current node
    free(n2);
    return;
}

// new function to check words recursively in linked list
bool checkword(node n3, const char *word)
{
    // temporary bool to store whether word exists
    bool status = true;

    // loop for every character
    for (int i = 0; i < strlen(word); i++)
    {
        // if there is a spelling error
        if (n3.word[i] != tolower(word[i]))
        {
            // set bool to false & exit
            status = false;
            break;
        }
    }

    // if no errors return true
    if (status)
    {
        return true;
    }
    // if different, but it connects to another node
    else if (n3.next != NULL)
    {
        // check word against next word in connecting node
        return checkword(*(n3.next), word);
    }
    // if errors & no connecting node - return false
    else
    {
        return false;
    }
}

// function to check size recursively
void checksize(node n4)
{
    // if word stored, increment counter
    if (n4.word[0] != 0)
    {
        numwords++;

        // if pointer also exists
        if (n4.next != NULL)
        {
            // check next node
            checksize(*n4.next);
        }
    }
    return;
}
