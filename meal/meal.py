def main():
    # get user input and convert
    time = input("What time is it? ")
    ntime = convert(time)

    # check time and output accordingly
    if ntime <= 8 and ntime >= 7:
        print("breakfast time")
    elif ntime <= 13 and ntime >= 12:
        print("lunch time")
    elif ntime <= 19 and ntime >= 18:
        print("dinner time")

def convert(time):
    # store hrs and minutes in list
    temp = time.split(":")
    temp[1] = (temp[1].split())[0]

    # if pm, add 12 to hrs
    if time.endswith("p.m."):
        temp[0] = int(temp[0]) + 12

    # calculate time in decimal hrs & return
    total = int(temp[0]) + (int(temp[1]) / 60)
    return total

if __name__ == "__main__":
    main()