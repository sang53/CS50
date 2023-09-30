while True:
    fuel = input("Fraction: ")
    nums = fuel.split("/")
    try:
        perc = int(nums[0]) / int(nums[1]) * 100
        if perc <= 100:
            break
    except:
        ...

if perc >= 99:
    print("F")
elif perc <= 1:
    print("E")
else:
    print(str(round(perc)) + "%")
