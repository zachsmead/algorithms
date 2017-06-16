import random

numbers = [0,1,2,3,4,5,6,7,8]

shuffled_numbers = random.sample(numbers, len(numbers))

def insertion_sort(array):
	print "sorting '%s'" % (array)

	
	for i in range(1, len(array)):
		key = array[i]
		for j in range(i - 1, -1, -1): 		# this is the range of elements to the left of array[i]
																			# compare each element to the key. 
																			# if key is less than the element, move the element to the right.
			if key < array[j]:
				array[j + 1] = array[j]
				array[j] = key
				# print '%d is less than array[%d] (%d)' % (key, j, array[j]) # for testing purposes
				# print array
			elif key > array[j]:
				array[j + 1] = key
				# print '%d is greater than array[%d] (%d)' % (key, j, array[j]) # for testing purposes
				# print array
				break
	return array

print insertion_sort(numbers)
print insertion_sort(shuffled_numbers)