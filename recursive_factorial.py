def recursive_factorial(number):
	if number == 0:
		return 1

	result = 1

	result = number * recursive_factorial(number - 1)

	return result

print recursive_factorial(3)
print recursive_factorial(5)

