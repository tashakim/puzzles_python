def iterBinsearch(arr, x):
	"""Purpose:
	"""
	low = 0
	hi = len(arr) -1

	while (low < hi):
		mid = (low + hi)//2
		if(arr[mid] == x):
			return True
		if(x < arr[mid]):
			low = mid +1
		if(x > arr[mid]):
			hi = mid -1

	return arr[low] == x

if __name__ == "__main__":
	arr = [5,4,3,2,1]
	print(iterBinsearch(arr, 6))
	print(iterBinsearch(arr, 4))
