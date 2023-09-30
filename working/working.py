import re


def main():
    print(convert(input("Hours: ")))


def convert(time):
    # check if matches format & get matches
    if nums := re.fullmatch(r"(\d\d?)(?:\:?)(\d\d)? (AM|PM) to (\d\d?)(?:\:?)(\d\d)? (AM|PM)", time):
        # get start hour, validate & convert to 24h
        start_hr = int(nums[1])
        valerr_range(start_hr, 12)
        start_hr = convert_hrs(start_hr, nums[3])

        # get start min, validate
        start_min = int_notNone(nums[2])
        valerr_range(start_min, 59)

        # get end hour, validate & convert to 24h
        end_hr = int(nums[4])
        valerr_range(end_hr, 12)
        end_hr = convert_hrs(end_hr, nums[6])

        # get end min, validate
        end_min = int_notNone(nums[5])
        valerr_range(end_min, 59)

    else:
        # ValueError if not meeting format
        raise ValueError

    # format string to output
    return f"{start_hr:02d}:{start_min:02d} to {end_hr:02d}:{end_min:02d}"

def int_notNone(number):
    # check if there is match, if None, return 0min
    if number != None:
        return int(number)
    else:
        return 0

def valerr_range(test, range):
    # check if test smaller than range
    if test > range:
        raise ValueError


def convert_hrs(hrs, meridiem):
    # convert to 24hr time, with special cases of 12AM & 12PM
    if meridiem == "PM" and hrs != 12:
        return hrs + 12
    elif hrs == 12 and meridiem == "AM":
        return 0
    else:
        return hrs


if __name__ == "__main__":
    main()
