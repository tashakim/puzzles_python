def mergesort(arr):
	"""Purpose: Simple python implementation of merge sort
	algorithm.
	"""
	mid = (l+r)//2
	left = arr[:mid]
	right = arr[mid:]

	mergesort(arr, left, mid)
	mergesort(arr, mid+1, right)

	merge(arr, left, mid, right)


if __name__ == "__main__":
