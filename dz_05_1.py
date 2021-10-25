with open("text.txt", 'w') as file:
    input_str = input('Введите строки:\n')
    while input_str:
        file.write(f'{input_str}\n')
        input_str = input('')