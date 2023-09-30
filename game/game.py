import random

while True:
    try:
        answer = random.randint(1, int(input("Level: ")))
        break
    except ValueError:
        pass


while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if guess == answer:
        print("Just right!")
        break
    elif guess < answer:
        print("Too small!")
    else:
        print("Too large!")
