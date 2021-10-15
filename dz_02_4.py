my_str = input('Введите строку из нескольких слов с пробелами: ')
word = my_str.split()
num = 0
for num, word in enumerate(word):
    print(f'{num + 1}) {word[:10]}')