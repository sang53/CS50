import sys
import csv

def main():
    # Error msg & exits for wrong CLA num
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check if python file
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # make sure file exists
    try:
        FILE = open(sys.argv[1], "r")
    except FileNotFoundError:
        err_str = "Could not read " + sys.argv[1]
        sys.exit(err_str)

    # create DictReader & DictWriter objects
    dict_reader = csv.DictReader(FILE)
    OUT_FILE = open(sys.argv[2], "w")
    dict_writer = csv.DictWriter(OUT_FILE, fieldnames=("first", "last", "house"))

    # write header into csv
    dict_writer.writeheader()

    # iterate each row, separate name
    # restructure data & write into new file
    for row in dict_reader:
        last, first = row["name"].split(", ")
        newrow = {"first": first, "last": last, "house": row["house"]}
        dict_writer.writerow(newrow)

    FILE.close()
    OUT_FILE.close()





if __name__ == "__main__":
    main()