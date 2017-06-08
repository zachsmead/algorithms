import random

numbers = [0,1,2,3,4,5,6,7,8]

shuffled_numbers = random.sample(numbers, len(numbers))

def selection_sort(array):

	print "sorting '%s'" % (array)

	comparing_index = 0
	# subarray = array[1:(array.length + 1)]
	
	for j in range(0, len(array)): # for j times, where j is the number of elements in the array
		for i in range(comparing_index + 1, len(array)): # for all elements to the right of comparing_index
			if array[i] < array[comparing_index]: # swap the two values
				holder = array[comparing_index]
				array[comparing_index] = array[i]
				array[i] = holder
		comparing_index += 1

	return array

print selection_sort(numbers)
print selection_sort(shuffled_numbers)