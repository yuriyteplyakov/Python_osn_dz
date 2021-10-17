def my_func(num_1, num_2, num_3):
    if num_1 >= num_2 and num_2 >= num_3:
        return num_1 + num_2
    elif num_1 >= num_3 and num_3 >= num_2:
        return num_1 + num_3
    elif num_2 >= num_1 and num_1 >= num_3:
        return num_1 + num_2
    elif num_2 >= num_3 and num_3 >= num_1:
        return num_2 + num_3
    elif num_3 >= num_1 and num_1 >= num_2:
        return num_1 + num_3
    elif num_3 >= num_2 and num_2 >= num_1:
        return num_3 + num_2
    # sum_nums = num_1 + num_2 + num_3
    # return sum_nums - min((num_1, num_2, num_3))
a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
print(my_func(num_1=a, num_2=b, num_3=c))