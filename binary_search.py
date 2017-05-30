import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def binary_search(array, target):

	min = 0
	max = len(array) - 1


	while min < max:
		mid = int((min + max) / 2)
		guess = array[mid]
		print 'searching for %d in %s' % (target, array)
		print 'guess: %d, index of guess: %d' % (guess, mid)

		if target == guess:
			return '%d was found at index %d' % (target, mid)
		elif guess < target:
			print 'guess was too low'
			if min == mid: # if the avg of min + max is still equal to mid, this means we've eliminated all other options already
										 # so we can tell the loop to break.
				break
			min = mid + 1
			print 'new min: %d' % min
		elif guess > target:
			print 'guess was too high'
			max = mid - 1
			print 'new max: %d' % max




print binary_search(primes, -2) # in this case, max will = -1 while min = 0, so the loop will break on its own, returning nothing.
print "*" * 100
print binary_search(primes, 17)
print "*" * 100
print binary_search(primes, 10)
print "*" * 100
print binary_search(primes, 100)
print "*" * 100

