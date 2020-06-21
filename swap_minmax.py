def swapMinMax(arr):
	"""Purpose: Design (1) swapping min and max indices in one
	method, (2) implemented in a more modular way, by 
	separating into two different methods.
	"""
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
	minIndex = getMinIndex(arr)
	maxIndex = getMaxIndex(arr)
	swapIndices(arr, minIndex, maxIndex)
	return arr

def getMinIndex(arr):
	return arr.index(min(arr))

def getMaxIndex(arr):
	return arr.index(max(arr))

def swapIndices(arr, minIndex, maxIndex):
	arr[minIndex], arr[maxIndex] = arr[maxIndex], arr[minIndex]
	return arr


if __name__ == "__main__":
	arr = [1,2,3,4,5]
	assert(swapMinMax(arr) == [5,2,3,4,1]), "Wrong answer"
	print("Test passed!")

	assert(modular_sol(arr) == swapMinMax(arr)), "Wrong answer"
	print("Second test passed!\n")

	print("All tests passed!")