import sys

def main():
    # Error msg & exits for wrong CLA num
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    # Check if python file
    if not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    # make sure file exists
    try:
        FILE = open(sys.argv[1], "r")
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    # open file and add counter if not comment or whitespace
    rows = FILE.readlines()
    counter = 0
    for row in rows:
        if row.isspace():
            continue
        elif comment(row):
            continue
        else:
            counter += 1

    print(counter)
    FILE.close()


def comment(row):
    # check if row starts with whitespace, then "#"
    temp = row.lstrip()
    return temp.startswith("#")



if __name__ == "__main__":
    main()