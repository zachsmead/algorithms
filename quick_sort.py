import sys
import time
import random

numbers = range(30)
shuffled_numbers = random.sample(numbers, len(numbers))

def quick_sort(array, low, hi):
	if low == 0 and hi == len(array) - 1:
		print 'sorting %s' % array
	if low < hi: # this means that there's more than 1 element in the input array
		p = partition(array, low, hi)
		quick_sort(array, low, p) # call quicksort on the subarray array[low:p]
		quick_sort(array, p + 1, hi) #  call quicksort on the subarray array[p + 1:hi]
	return array



def partition(array, low, hi): # this function 'partitions' the input array into subarrays

	print 'PARTITION [%s:%s]' % (low, hi)

	pivot_index = get_pivot(array, low, hi)
	pivot_value = array[pivot_index]
	border = low # all elements that are less than pivot_value will be placed left of the border
	
	array[pivot_index], array[low] = array[low], array[pivot_index] # swap the pivot to array[low]

	for i in range (low, hi + 1): # loop through the subarray. if the element at [i] < pivot_value, increment
																# border and swap border with the element at position [i].
																# this keeps all elements that are < pivot_value, on left side of subarray
		print array
		print 'loop index: % s comparison value: % s' % (i, array[i])
		print 'border position: % s - border value: % s' % (border, array[border])
		print 'pivot value: % s' % pivot_value
		if array[i] < pivot_value:
			border += 1
			array[i], array[border] = array[border], array[i]

	array[low], array[border] = array[border], array[low]

	print 'final border value for this partition: % s at position %s' % (array[border], border)

	print '*' * 100
	return border # return the index of the last element that is less than pivot_value




def get_pivot(array, low, hi): # this function contains a conditional that gives the median of 3 points
	mid = (hi + low) // 2

	pivot_index = hi

	if array[low] < array[mid]:
		if array[mid] < array[hi]:
			pivot_index = mid
	elif array[low] < array[hi]:
			pivot_index = low
	return pivot_index

print quick_sort(shuffled_numbers, 0, len(numbers) - 1)


