def convert(userinput):
    userinput = userinput.replace(":)", "🙂")
    return userinput.replace(":(", "🙁")

def main():
    userinput = input()
    userinput = convert(userinput)
    print(userinput)

main()