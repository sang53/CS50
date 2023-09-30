import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print('Usage: python dna.py data.csv sequence.txt')

    # Read database file into a variable
    database = {}
    with open(sys.argv[1]) as data:
        # save keys into separate list
        key = data.readline()
        key.rstrip('\n')
        keys = key.split(',')
        # reset position of file
        data.seek(0)
        # input csv contents in nested dictionary
        input = csv.DictReader(data)
        for people in input:
            database[people[keys[0]]] = people
            database[people[keys[0]]].pop(keys[0])

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as tester:
        sequence = tester.read()

    # Find longest match of each STR in DNA sequence
    testdict = {}
    for subsequence in database[list(database.keys())[0]]:
        testdict.update({subsequence: str(longest_match(sequence, subsequence))})

    # Check database for matching profiles
    for people in database:
        if database[people] == testdict:
            print(people)
            exit()

    # no match case
    print('No match\n')
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
