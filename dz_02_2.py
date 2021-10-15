input_list = input('Введите список: ')
print(input_list)
my_input = input_list.split()
i = 0

while i < len(my_input) - 1:
    my_input[i], my_input[i + 1] = my_input[i + 1], my_input[i]
    i += 2
print(my_input)



