import sys
from pyfiglet import Figlet
import random


def main():
    # if no CLA, print random font
    if len(sys.argv) == 1:
        printfiglet(rand_font())

    # if CLA given, check validity and print in output font
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            printfiglet(sys.argv[2])

        else:
            invalid()

    else:
        invalid()


def invalid():
    # exit with error msg
    sys.exit("Invalid usage")


def printfiglet(output_font):
    # try to set output font, exit if invalid
    figlet = Figlet()
    try:
        figlet.setFont(font=output_font)
    except:
        invalid()

    # get user input str and output figlet
    user_input = input("Input: ")
    print(figlet.renderText(user_input))


def rand_font():
    # return random font from list
    figlet_rand = Figlet()
    font_list = figlet_rand.getFonts()
    return font_list[random.randrange(0, len(font_list) - 1)]


main()