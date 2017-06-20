import math
import random

numbers = range(0, 101)

shuffled_numbers = random.sample(numbers, len(numbers))

def merge_sort(array, first, last):

	print 'sorting %s' % array[first:last]
	
	if first < last:	
		middle = int((first + last) / 2)
		merge_sort(array, first, middle)
		merge_sort(array, middle + 1, last)
		merge(array, first, middle + 1, last)

	return array


def merge(array, first, middle, last):
	l = array[first:middle]
	r = array[middle:last + 1]

	l.append(9999999)
	r.append(9999999)
	i, j = 0, 0

	for k in range (first, last + 1):
		if l[i] <= r[j]:
			array[k] = l[i]
			i += 1
		else:
			array[k] = r[j]
			j += 1


print merge_sort(shuffled_numbers, 0, len(numbers) - 1)
# print merge_sort([1], 0, 0)