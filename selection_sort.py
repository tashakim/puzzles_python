def selection_sort(arr):
	"""Purpose: Python implementation of selection sort.
	"""
	n = len(arr)
	for i range(n-2):
		min = argmin(arr[i: n-1])
		arr[i] = arr[min]
	return arr

if __name__ == "__main__":
	a = [4,5,1,2,3,6]
	selection_sort(a)