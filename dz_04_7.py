import math
def generator(number):
	factorial = 1
	for i in range(1, number + 1):
		factorial *= i
		yield factorial
n = 52
for ind, el in enumerate(generator(n)):
	print(f"{ind + 1}) {el}")