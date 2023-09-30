# get user input
input_str = input("Input: ")

# set up output string and list of vowels
output_str = ""
vowels = ["a", "e", "i", "o", "u"]

# iterate through every char and add to output string if not in vowels
for char in input_str:
    if char.lower() not in vowels:
        output_str += char

# print output
print("Output: " + output_str)