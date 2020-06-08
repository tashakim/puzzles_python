def selection_sort(arr):
	"""Purpose: Python implementation of selection sort.
	"""
	n = len(arr)
	for i in range(n-2):
		min = argmin(arr[i: n-1])
		arr[i] = arr[min]
	return arr

def argmin(arr):
	"""Purpose: Simple helper method that returns the 
	minimum element in an input array.
	"""



if __name__ == "__main__":
	a = [4,5,1,2,3,6]
	assert(selection_sort(a) == [1,2,3,4,5,6]), "Wrong answer"
	print("All tests passed!")