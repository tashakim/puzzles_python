import pytest

class InvalidInputException(Exception):
	pass

def swapMinMax(arr):
	"""Purpose: Design (1) swapping min and max indices in one
	method, (2) implemented in a more modular way, by 
	separating into two different methods.
	"""
	if(arr is None or len(arr) < 2):
		raise InvalidInputException("Input is invalid.")

	minIndex, maxIndex = 0, 0
	for i in range(len(arr)):
		if(arr[i] < arr[minIndex]):
			minIndex = i

	for i in range(len(arr)):
		if(arr[i] > arr[maxIndex]):
			maxIndex = i

	arr[minIndex], arr[maxIndex] = arr[maxIndex], arr[minIndex]
	return arr


def modular_sol(arr):
	if(arr is None or len(arr) < 2):
		raise InvalidInputException("Input is invalid.")

	minIndex = getMinIndex(arr)
	maxIndex = getMaxIndex(arr)
	swapIndices(arr, minIndex, maxIndex)
	return arr

def getMinIndex(arr):
	"""Purpose: Helper method for modular_sol()
	Output: index of 'arr' that contains minimum integer
	"""
	return arr.index(min(arr))

def getMaxIndex(arr):
	"""Purpose: Helper method for modular_sol()
	Output: index of 'arr' that contains maximum integer
	"""
	return arr.index(max(arr))

def swapIndices(arr, minIndex, maxIndex):
	"""Purpose: Helper method for modular_sol()
	Output: 'arr', with minimum and maximum indices swapped.
	"""
	arr[minIndex], arr[maxIndex] = arr[maxIndex], arr[minIndex]
	return arr

def testValidInput():
	"""Purpose: Tests that both methods raise correct 
	Exception when invalid input is given.
	"""
	with pytest.raises(InvalidInputException):
		swapMinMax([])
		swapMinMax(None)
		swapMinMax([0])

		modular_sol([])
		modular_sol(None)
		modular_sol([3])


if __name__ == "__main__":
	arr = [1,2,3,4,5]
	assert(swapMinMax(arr) == [5,2,3,4,1]), "Wrong answer"
	print("Test passed!")

	assert(modular_sol(arr) == swapMinMax(arr)), "Wrong answer"
	print("Second test passed!\n")
	testValidInput()

	print("All tests passed!")