my_list = [1, 2, 5, 1, 10, 15]

new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]

print(new_list)