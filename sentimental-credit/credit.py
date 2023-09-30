# Get user input until valid number given
while True:
    number = input("Number: ")
    if number.isdigit():
        break

# Initialise dictionary of starting numbers
dict = {}
dict2 = {}
dict['AMEX'] = ['34', '37']
dict2['AMEX'] = [15]
dict['MASTERCARD'] = ['51', '52', '53', '54', '55']
dict2['MASTERCARD'] = [16]
dict['VISA'] = ['4']
dict2['VISA'] = [13, 16]

# Iterate through dict to find type of card
for type in dict:
    for i in range(len(dict[type])):
        if number.startswith(dict[type][i]):
            if len(number) in dict2[type]:
                card_type = type
                break

# if card_type empty print INVALID
try:
    card_type.upper()
except NameError:
    print('INVALID')
    exit()

# checksum if valid start
# temp dict to store variables
sums = {'count': 0, 'even': 0, 'odd': 0}
# reverse number order
number = number[::-1]

# add to appropriate dictionary key for every digit
for i in number:
    if sums['count'] % 2 == 0:
        sums['even'] += int(i)
    else:
        # use divmod to separate digits in 2 digit number
        sums['odd'] += sum(divmod(int(i) * 2, 10))
    # counter for even/odd
    sums['count'] += 1

# checksum using even & odd sums
legit = str(sums['even'] + sums['odd'])

# check if checksum ends in 0
if legit.endswith('0'):
    print(card_type)
else:
    print('INVALID')