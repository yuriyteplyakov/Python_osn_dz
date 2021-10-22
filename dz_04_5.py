from functools import reduce

my_list = [i for i in range(99, 1001) if i % 2 == 0]

print(reduce((lambda x, i: x * i), my_list))