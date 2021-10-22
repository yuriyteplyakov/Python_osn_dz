from itertools import cycle, count
n = 100
my_list = [x for x in range(5)]
counter = count()
cycler = cycle(my_list)
print(next(counter) for x in range(n))
print(next(cycler) for x in range(n))