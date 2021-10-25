with open("text_2.txt") as file:
    content = file.readlines()
    count = 0
    for num, line in enumerate(content):
        print(f'строка - {num + 1}) количество слов в строке - {len(line.split())}')
        count += 1
    print(f'Количество строк - {count}')