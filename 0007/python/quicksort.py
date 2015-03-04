def quicksort(array):
	less = []
	greater = []
	if len(array)<=1:
		return array
	pivot = array.pop()
	for x in array:
		if x<pivot: less.append(x)
		else: greater.append(x)
	return quicksort(less)+[pivot]+quicksort(greater)