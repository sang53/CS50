import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.fullmatch(r"\d+\.\d+\.\d+\.\d+", ip):
        addys = ip.split(".")
        for addy in addys:
            if int(addy) > 255:
                return False
        return True
    else:
        return False




if __name__ == "__main__":
    main()