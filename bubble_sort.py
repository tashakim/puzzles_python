def bubbleSort(arr):
	"""Purpose: Python implementation of a bubble sorting algorithm.
	"""
	for i in range(len(arr)):
		for j in range(len(arr)-i):
			if(arr[j] > arr[j+1]):
				arr[j], arr[j+1] = arr[j+1], arr[j]

	return arr

if __name__ == "__main__":
	a = [32,30,0,1,2]
	print(bubbleSort(a))