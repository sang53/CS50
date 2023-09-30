// Simulate genetic inheritance of blood type

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
}
person;

int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();

int main(void)
{
    // Seed random number generator
    srand(time(0));
    printf("Enter the number of generations: ");
    scanf("%i", &GENERATIONS);
    // Create a new family with three generations
    person *p = create_family(GENERATIONS);

    // Print family tree of blood types
    print_family(p, 0);

    // Free memory
    free_family(p);
}

// Create a new individual with `generations`
person *create_family(int generations)
{
    // TODO: Allocate memory for new person
    person *child = malloc(sizeof(person));
    // If there are still generations left to create
    if (generations > 1)
    {
        // Create two new parents for current person by recursively calling create_family
        person *parent[2];
        for (int i = 0; i < 2; i++)
        {
            parent[i] = create_family(generations - 1);
        }

        // Set parent pointers for current person
        child->parents[0] = parent[0];
        child->parents[1] = parent[1];

        // Randomly assign current person's alleles based on the alleles of their parents
        for (int i = 0; i < 2; i++)
        {
            int r = rand() % 2;
            child->alleles[i] = parent[i]->alleles[r];
        }
    }
    // If there are no generations left to create
    else
    {
        // Set parent pointers to NULL & Randomly assign alleles
        for (int i = 0; i < 2; i++)
        {
            child->parents[i] = NULL;
            child->alleles[i] = random_allele();
        }
    }

    // Return newly created person
    return child;
}

// Free `p` and all ancestors of `p`.
void free_family(person *p)
{
    // free parents recursively
    if (p->parents[0] != NULL)
    {
        free_family(p->parents[0]);
        free_family(p->parents[1]);
    }

    // free current person
    free(p);
}

// Print each family member and their alleles.
void print_family(person *p, int generation)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Print indentation
    for (int i = 0; i < generation * INDENT_LENGTH; i++)
    {
        printf(" ");
    }

    // Print person
    if (generation == 0)
    {
        printf("Child (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else if (generation == 1)
    {
        printf("Parent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else
    {
        for (int i = 0; i < generation - 2; i++)
        {
            printf("Great-");
        }
        printf("Grandparent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }

    // Print parents of current generation
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}

// Randomly chooses a blood type allele.
char random_allele()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
