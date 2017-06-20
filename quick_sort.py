import sys
import time
import random

numbers = range(30)
shuffled_numbers = random.sample(numbers, len(numbers))

def quick_sort(array, low, hi):

	print ('%s' % array)
	sys.stdout.flush()
	time.sleep(0.01)

	if low < hi: # this means that there's more than 1 element in the input array
		p = partition(array, low, hi) 
		quick_sort(array, low, p) # call quicksort on the subarray array[low:p]
		quick_sort(array, p + 1, hi) #  call quicksort on the subarray array[p + 1:hi]
	return array



def partition(array, low, hi): # this function 'partitions' the input array into 
	pivot_index = get_pivot(array, low, hi)
	pivot_value = array[pivot_index]
	border = low # the border 

	array[pivot_index], array[low] = array[low], array[pivot_index] # swap pivot with the element at partition[0]

	for i in range (low, hi + 1):
		if array[i] < pivot_value:
			border += 1
			array[i], array[border] = array[border], array[i]
	array[low], array[border] = array[border], array[low]
	return border # return the border of the new partition




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


