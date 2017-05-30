import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def binary_search(array, target):

	min = 0
	max = len(array) - 1


	while min < max:
		mid = int((min + max) / 2)
		print 'searching for %d in %s' % (target, array)
		print 'guess: %d' % array[mid]
		guess = array[mid]
		if target == guess:
			return '%d was found at index %d' % (target, mid)
		elif guess < target:
			print 'guess was too low'
			if min == mid: # this means the element is not found in the array
				break
			min = mid + 1
		elif guess > target:
			print 'guess was too high'
			max = mid - 1





print binary_search(primes, 72)
print binary_search(primes, 17)
print binary_search(primes, 10)
print binary_search(primes, 100)

