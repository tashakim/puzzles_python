class InvalidInputException:
	"""Purpose: Exception will be thrown when input array is
	invalid.
	"""
	pass

def bubbleSort(arr):
	"""Purpose: Python implementation of a bubble sorting algorithm.
	"""
	if(arr == None or arr == []):
		raise InvalidInputException("Input is invalid")

	for i in range(len(arr) -1):
		for j in range(len(arr)-i -1):
			if(arr[j] > arr[j+1]):
				arr[j], arr[j+1] = arr[j+1], arr[j]

	return arr


if __name__ == "__main__":
	a = [32,30,0,1,2]
	a2 = [0,0,0,1,0]
	a3 = [-1,4,-5,9,11]
	assert(bubbleSort(a) == [0,1,2,30,32]), "Wrong order"
	assert(bubbleSort(a2) == [0,0,0,0,1]), "Wrong order"
	assert(bubbleSort(a3) == [-5,-1,4,9,11]), "Wrong order"

	print("All tests passed!") 