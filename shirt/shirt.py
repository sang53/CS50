import sys
import csv
from PIL import Image, ImageOps

def main():
    # Error msg & exits for wrong CLA num
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check if extension are valid
    if not valid_extension(sys.argv[1]) or not valid_extension(sys.argv[2]):
        sys.exit("Invalid file types")

    if sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit("Different file extensions")

    # make sure file exists
    try:
        input = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        err_str = "Could not read " + sys.argv[1]
        sys.exit(err_str)

    # resize input img to shirt size
    size = shirt.size
    new_input = ImageOps.fit(input, size)

    # paste & save pasted image
    new_input.paste(shirt, shirt)
    new_input.save(sys.argv[2])


def valid_extension(input):
    # check if input ends in valid extension
    input = input.lower()
    if input.endswith(".jpg") or input.endswith(".jpeg") or input.endswith(".png"):
        return True
    else:
        return False


if __name__ == "__main__":
    main()