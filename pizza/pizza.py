import csv
from tabulate import tabulate
import sys

table_format = "grid"

def main():
    # Error msg & exits for wrong CLA num
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if python file
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # make sure file exists
    try:
        FILE = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")

    # make reader obj & create table list
    dict = csv.reader(FILE)
    table = []

    # add each row to table
    for row in dict:
        table.append(row)

    # print table
    print(tabulate(table, headers="firstrow", tablefmt=table_format))


if __name__ == "__main__":
    main()