def main():
    camelCase = input("camelCase: ")
    snake_case = snake(camelCase)
    print("snake_case: " + snake_case)

def snake(camel):
    snake = ""
    for char in camel:
        if char.isupper():
            snake += ("_" + char.lower())
        else:
            snake += char
    return snake



if __name__ == "__main__":
    main()