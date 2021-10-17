def my_func(x, y):
    if x < 0:
        return print('Наверное, Вы хотели ввести х больше нуля?')
    if y > 0:
        return print('Наверное, Вы хотели ввести у меньше нуля?')
    rezult = 1
    for i in range(abs(y)):
        a = 1 / x
        rezult *= a
    return rezult

x = float(input('Введите положительное число х: '))
y = int(input('Введите отрицательное число y: '))

print(my_func(x, y))