from datetime import date, timedelta
import sys
import inflect

p = inflect.engine()


def main():
    # get user input, convert to date obj, calculate difference to today
    time_diff = date.today() - convert(input("Date of Birth: "))

    # convert timedelta obj to int(minutes)
    minutes = int(time_diff.total_seconds() / 60)

    # convert to English & print
    print((p.number_to_words(minutes).capitalize() + " minutes").replace(" and ", " "))


def convert(string):
    # split input into separate numbers
    nums = string.split("-")

    try:
        # if year is in the future, exit
        if int(nums[0]) > date.today().year:
            sys.exit("Invalid year")

        # return date obj using input
        return date(int(nums[0]), int(nums[1]), int(nums[2]))
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()