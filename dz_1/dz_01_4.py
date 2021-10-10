num = int(input("Введите целое положительное число: "))
num_ost = 0
num_max = 0
while num > num_ost:
    num_ost = num // 10
    if num_ost > 0:
        num_max = num % 10
        print(num_max)
    elif num_max == 9:
        break
    else:
        print(f'Самая большая цифра в числе: {num_max}')

