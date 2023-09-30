while True:
    num_s = input('Heignt: ')
    if num_s.isdigit() == True:
        num_i = int(num_s)
        if num_i > 0 and num_i < 9:
            break

mario = '{0}{1}  {1}'
for i in range(1, num_i + 1):
    print(mario.format(' ' * (num_i - i), '#' * i))
