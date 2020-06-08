def selection_sort2(arr):
	"""Purpose: Simple python implementation of selection sorting algorithm.
	"""
	for i in range(len(arr)):
		min_index = i
		for j in range(i+1, len(arr)):
			if(arr[min_index] > arr[j]):
				min_index = j
		arr[i], arr[min_index] =  arr[min_index], arr[i]
	return arr


if __name__ == "__main__":
	a = [5,3,2,4,1]
	assert(selection_sort2(a) == [1,2,3,4,5]), "Wrong answer"
	print("All tests passed!")