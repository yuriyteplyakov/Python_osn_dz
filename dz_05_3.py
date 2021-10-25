with open('text_3.txt') as file:
    content = file.readlines()
    staffs = {}
    sum_salary = 0
    for line in content:
        staff_info = line.split()
        staffs.update({int(staff_info[0]): staff_info[1]})#если поменять местами в файле с текстом значения, выдает ошибку IndexError: list index out of range
        sum_salary += int(staff_info[0])
avarge_salary = sum_salary / len(staffs)
print(f'Средняя зарплата в компании составляет: {avarge_salary}')
for k, v in staffs.items():
    if k < 20000:
        print(f'{k}: {v}')