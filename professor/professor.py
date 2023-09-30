import random

def main():

    # get level & initialise variables
    level = get_level()
    score = 0

    # loop for 10 problems
    for _ in range(10):

        # generate random numbers
        x = generate_integer(level)
        y = generate_integer(level)

        # loop for 3 guesses
        for guess in range(3):

            # get answer while checking type
            try:
                answer = int(input(str(x) + " + " + str(y) + " = "))
            except ValueError:
                pass
            else:
                # if answer wrong, add score and break loop
                if answer == x + y:
                    score += 1
                    break

            # if answer wrong or invalid
            print("EEE")

            # if last guess, print answer
            if guess == 2:
                print(x, "+", y, "=", x + y)

    # print score
    print("Score:", score)


def generate_integer(level):
    # generate random int of level digits
    if level == 1:
        # special case as 0 included at level 1 
        return random.randint(0, 9)
    else:
        return random.randint(pow(10, level - 1), pow(10, level) - 1)


def get_level():
    # loop until valid input
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        # check level & return value if 1-3
        if level in (1, 2, 3):
            return level


if __name__ == "__main__":
    main()