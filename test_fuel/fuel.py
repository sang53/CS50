def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue

        try:
            output = gauge(percentage)
        except TypeError:
            continue
        else:
            print(output)
            break


def convert(fraction):
    nums = fraction.split("/")
    perc = round(int(nums[0]) / int(nums[1]) * 100)
    if perc > 100 or perc < 0:
        raise ValueError()
    else:
        return perc


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()




