total = 0

while total < 50:
    print("Amount Due: " + str(50 - total))
    coins = input("Insert Coin: ")
    if coins == "25":
        total += 25
    elif coins == "10":
        total += 10
    elif coins == "5":
        total += 5

print("Change Owed: " + str(total - 50))