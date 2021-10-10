profit = int(input("Введите прибыль вашей фирмы:"))
costs = int(input("Введите издержки вашей фирмы:"))
if profit > costs:
    rentab = (profit - costs) / profit
    print(f'У вас есть прибыль, рентабельность выручки составила {rentab}')
    employees = int(input("Введите численность сотрудников вашей фирмы: "))
    employees_profit = profit / employees
    print(f'прибыль фирмы в расчете на одного сотрудника составила, {employees_profit}')
elif profit == costs:
    print('Вы вышли в ноль')
else:
    print('Вы терпите убытки')
