my_list = [7, 5, 3, 2, 1]
new = int(input('Введите число:'))
my_list.append(new)
for index, elem in enumerate(my_list):
    if new > elem:
        my_list.insert(index, new)
        my_list.pop()
        print(my_list)
        break
    elif new == elem:
        my_list.insert(index + 1, new)
        my_list.pop()
        print(my_list)
        break


