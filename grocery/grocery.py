groceries = {}
while True:
    try:
        item = input("")
        item = item.upper()
        groceries[item] += 1
    except EOFError:
        print("\n")
        break
    except KeyError:
        groceries.update({item: 1})
    except:
        continue

keys = list(groceries)
keys.sort()

for item in keys:
    print(groceries[item], item)