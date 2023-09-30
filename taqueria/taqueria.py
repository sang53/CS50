menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
order = "temp"
while(True):
    try:
        order = input("Item: ")
        total += menu[order.title()]
        print("Total: $" + "{:.2f}".format(total))
    except EOFError:
        print("\n")
        break
    except:
        continue


print("Total: $" + "{:.2f}".format(total))