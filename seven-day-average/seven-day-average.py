import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    tempdict = {}

    for entries in reader:
        tempdict.setdefault(entries['state'], []).append(entries['cases'])
    for keys in tempdict:
        del tempdict[keys][0:-15]
        tempdict[keys].reverse()
        for cases in range(0, len(tempdict[keys]) - 1):
            tempdict[keys][cases] = int(tempdict[keys][cases]) - int(tempdict[keys][cases + 1])
        del tempdict[keys][-1]
    return tempdict




# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        nave = sum(new_cases[state][0:6]) / 7
        oave = sum(new_cases[state][7:13]) / 7
        print(f'{state} had 7-day average of: {round(nave)}', end = ' ')
        if nave > oave:
            print('and a increase of', (nave - oave) / oave)
        elif oave > nave:
            print('and a decrease of', (oave - nave) / oave)
        else:
            print('which was the same as last week')


main()
