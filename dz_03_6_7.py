def int_func(text):
    word = text[0].upper() + text[1:].lower()
    return word
my_str = input('Введите строку: ')
print(int_func(my_str))

words = my_str.split()
for word in words:
    print(f'{int_func(word)}', end=' ')
