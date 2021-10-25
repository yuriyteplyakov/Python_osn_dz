with open("text_5.txt", 'w') as file:
    input_num = input('Введите числа разделенные пробелами:')
    file.write(f'{input_num}')
with open("text_5.txt") as file:
    content = file.read().split()
    sum = 0
    for num in content:
        sum += int(num)
print(sum)