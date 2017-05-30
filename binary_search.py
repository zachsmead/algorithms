import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def binary_search(numbers, number):
	print 'searching for', number, 'in', numbers

	# min = numbers[0]
	min = 0
	max = len(numbers)
	halfway = int(math.ceil(max / 2))



	if max < min:
		return -1
	elif (number == numbers[halfway]):
		return halfway
	elif (number > numbers[halfway]):
		print 'too low'
		min = halfway + 1
		new_numbers = numbers[min:]
		return binary_search(new_numbers, number)
	elif (number < numbers[halfway]):
		print 'too high'
		halfway = halfway - 1
		new_numbers = numbers[:halfway]
		return binary_search(new_numbers, number)




print binary_search(primes, 17)
print binary_search(primes, 10)
print binary_search(primes, 100)

