def sum_nums(my_str, stop):
    nums = my_str.split()
    sum_list = 0
    stop = 'stop'
    for num in nums:
        if num == stop:
            break
        sum_list += int(num)
    return sum_list

stopper = 'stop'
finished = False
sum = 0
while not finished:
    user_str = input('Введите строку из чисел разделенных пробелами:')
    sum += sum_nums(user_str, stopper)
    finished = stopper in user_str
    print(f'sum = {sum}')
