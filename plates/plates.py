def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # check alphanumeric, length, starts with 2 letters
    if not plate.isalnum():
        return False
    elif len(plate) < 2 or len(plate) > 6:
        return False
    elif not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    # check chars until not letters
    index = 2
    while(plate[index].isalpha()):

        # if only letters, return true
        if index == len(plate) - 1:
            return True

        index += 1

    # make sure numbers does not start with 0
    if plate[index] == "0":
        return False

    # make sure plate ends in numbers
    while(plate[index].isnumeric()):
        if index == len(plate) - 1:
            return True

        index += 1

    # return false if ends with letters
    return False



main()