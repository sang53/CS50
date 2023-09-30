from re import split


# define function to remove unwanted strings
def removestring(listofstrings, toremove):
    n = listofstrings.count(toremove)
    for _ in range(n):
        listofstrings.remove(toremove)


# get input text from user
text = input('Text: ').lower()

# split it into sentences & remove empty strings from list
sentences = split('\. *|\? *|\! *', text)
removestring(sentences, '')
removestring(sentences, ' ')

# take care of double punctuation cases
for letters in sentences:
    if len(letters) < 3 and not letters.isalpha():
        sentences.remove(letters)


# save number of sentences
nsentences = len(sentences)

# split text into words & remove empty strings
words = split(' ', text)
removestring(words, '')

#save number of words
wordn = len(words)

# count number of leters
nletters = 0
for letters in text:
    if letters.isalpha():
        nletters += 1

# calculate index
aveL = 100 * nletters / wordn
aveS = 100 * nsentences / wordn
index = 0.0588 * aveL - 0.296 * aveS - 15.8

# prep output string according to index & print
if index < 1:
    outputstring = 'Before Grade 1'
elif index >= 16:
    outputstring = 'Grade 16+'
else:
    outputstring = 'Grade {}'.format(round(index))

print(outputstring)
