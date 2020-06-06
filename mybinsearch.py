def binarysearch(arr, x):
	"""Purpose: Python implementation of binary search.
	Runtime: O(n)
	"""
	if(len(arr) == 0):
		return False

	if(len(arr) == 1):
		return arr[0] == x

	mid = len(arr)//2

	if(x ==  arr[mid]):
		return True
	if(x > arr[mid]):
		return binarysearch(arr[mid+1:],x)

	if(x < arr[mid]):
		return binarysearch(arr[:mid],x)


if __name__ == "__main__":
	a = [1,2,3,4,5]
	assert(binarysearch(a, 3) == True), "Wrong answer"
	assert(binarysearch(a, 5) == True), "Wrong answer"
	assert(binarysearch(a, 6) == False), "Wrong answer"

	print("All tests passed!")