import re


def main():
    print(parse(input("HTML: ")))


def parse(html):
    if html.startswith("<iframe") and html.endswith("</iframe>"):
        strings = html.split('"')
        for string in strings:
            if re.fullmatch(r"http[s]?://(www.)?youtube.com/embed/\w+", string):
                return "https://youtu.be/" + string.split("/")[4]

    return None



if __name__ == "__main__":
    main()