class InvalidInputException:
	"""Purpose: Exception will be raised when array input
	is invalid.
	"""
	pass

def selection_sort2(arr):
	"""Purpose: Simple python implementation of selection sorting algorithm.
	"""
	if(arr == None or arr == []):
		raise InvalidInputException("Array is invalid.")

	for i in range(len(arr)):
		min_index = i
		for j in range(i+1, len(arr)):
			if(arr[min_index] > arr[j]):
				min_index = j
		arr[i], arr[min_index] =  arr[min_index], arr[i]
	
	return arr


def bubble_sort(arr):
	"""Purpose:  Simple python implementation of bubble sorting algorithm.
	"""
	if(arr == None or arr == []):
		raise InvalidInputException("Array is invalid.")

	for i in range(len(arr)):
		for k in range(len(arr) -i):
			if(arr[k] > arr[k+1]):
				arr[k], arr[k+1]  = arr[k+1], arr[k]
	return arr


def insertion_sort(arr):
	"""Purpose: Simple python implementation  of insertion sorting
	algorithm.
	"""
	if (arr == None or arr == []):
		raise InvalidInputException("Array is invalid.")

	for i in range(1, len(arr)):
		el = arr[i]
		k = i-1

		while(k >= 0 and el < arr[k])
			arr[k+1] = arr[k]
			k -=1
		arr[k+1] = el
	
	return arr


if __name__ == "__main__":
	a = [5,3,2,4,1]
	b = [23,41,50,0,3]
	assert(selection_sort2(a) == [1,2,3,4,5]), "Wrong answer"
	assert(selection_sort2(b) == [0,3,23,41,50]), "Wrong answer"
	assert(bubble_sort(a) == [1,2,3,4,5]), "Bubble sort wrong"
	assert(bubble_sort(b) == [0,3,23,41,50]), "Bubble sort wrong"

	print("All tests passed!")
