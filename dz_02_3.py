num_month = int(input('Введите любой номер месяца от 1 до 12: '))
month_list = ['winter', 'spring', 'summer', 'autumn']
month_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if num_month <= 2 or num_month == 12:
    print(month_list[0])
    print(month_dict.get(1))
    print(month_dict[1])
elif 3 < num_month <= 5:
    print(month_list[1])
    print(month_dict[2])
elif 5 < num_month <= 8:
    print(month_list[2])
    print(month_dict[3])
else:
    print(month_list[3])
    print(month_dict[4])