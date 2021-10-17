def division(num_1, num_2):
    if num_2 == 0:
        return ('Ошибка! Деление на ноль!')
    else:
        return num_1 / num_2

num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
print(division(num_1, num_2))