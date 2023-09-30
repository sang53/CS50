import re


def main():
    print(count(input("Text: ")))


def count(input_str):
    matches = re.findall(r"\bum\b", input_str.lower())
    return len(matches)



if __name__ == "__main__":
    main()