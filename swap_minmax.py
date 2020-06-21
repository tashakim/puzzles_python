def swapMinMax(arr):
	"""Purpose: Design (1) swapping min and max indices in one
	method, (2) implemented in a more modular way, by 
	separating into two different methods.
	"""
	minIndex = 0
	for i in range(len(arr)):
		if(arr[i] < arr[minIndex]):
			minIndex = i

	maxIndex = 0
	for i in range(len(arr)):
		if(arr[i] > arr[maxIndex]):
			maxIndex = i

	temp = arr[minIndex]
	arr[minIndex] = arr[maxIndex]
	arr[maxIndex] = temp
	return arr

def modular_sol(arr):
	return

if __name__ == "__main__":
	arr = [1,2,3,4,5]
	assert(swapMinMax(arr) == [5,2,3,4,1]), "Wrong answer"
	print("Test passed!")