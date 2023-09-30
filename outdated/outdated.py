mths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    while True:
        # get input date and capitalise to check against mths list
        date = input("Date: ")
        date = date.capitalize()

        # get formatted string of new date
        new_date = dateify(date)

        # check if days & months are in range
        # loop if not meeting criteria
        try:
            nums = new_date.split("-")
            if int(nums[2]) <= 0 or int(nums[2]) > 31 or int(nums[1]) <= 0 or int(nums[1]) > 12:
                continue
            else:
                break
        except:
            continue

    # print output
    print(new_date)


def dateify(date):
    """takes date and outputs formatted string"""

    # set initial variables for scope
    year = 0
    month = 0
    day = 0

    # if Month day, year format
    if date[0].isalpha():

        # check if correct month and save month number
        for mth in mths:
            if mth in date:
                month = mths.index(mth) + 1
                break

        # if month not found return None
        if month == 0:
            return None

        # split string into parts and save day & year
        # if cannot be converted to int or no comma, return None
        sep_date = date.split(" ")
        try:
            if not sep_date[1].endswith(","):
                return None
            day = int(sep_date[1].rstrip(","))
            year = int(sep_date[2])
        except:
            return None

    # case for MM/DD/YYYY format
    else:
        # split string & save mth, day, year
        # if not int, return None
        sep_date = date.split("/")
        try:
            month = int(sep_date[0])
            day = int(sep_date[1])
            year = int(sep_date[2])
        except:
            return None

    # format using year, month, day and return formatted string
    new_date = format_date(year, month, day)
    return new_date


def format_date(year, month, day):
    # add year into string
    new_date = str(year) + "-"

    # add 0 in front if < 10, otherwise add to string
    if month < 10:
        new_date += "0" + str(month)
    else:
        new_date += str(month)

    new_date += "-"

    # add 0 in front if < 10, otherwise add to string
    if day < 10:
        new_date += "0" + str(day)
    else:
        new_date += str(day)

    # return formatted string
    return new_date


main()


