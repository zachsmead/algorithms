def iterative_factorial(number):
	result = 1

	for i in range(1, number + 1):
		result = result * i

	return result


print iterative_factorial(3)
print iterative_factorial(5)