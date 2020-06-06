def in_placeBinSearch(arr, hi, low, x):
	"""Purpose: Python implementation of recursive in-place binary search.
	Runtime: O(log(n))
	"""
	if(low == hi):
		return arr[low] == x

	mid = (low + hi)//2

	if(x == arr[mid]):
		return True

	if(x > arr[mid]):
		return in_placeBinSearch(arr, low, mid+1, x)
	if(x < arr[mid]):
		return in_placeBinSearch(arr, mid, hi, x)



if __name__  == "__main__":
	a  = [1,2,3,4,5]
	b  = [3]
	assert(in_placeBinSearch(a, 0, len(a)-1, 3) == True), "Wrong answer"
	assert(in_placeBinSearch(a, 0, len(a)-1, 4) == True), "Wrong answer"
	assert(in_placeBinSearch(b, 0, len(b)-1, 0) == False), "Wrong answer"
	assert(in_placeBinSearch(b, 0, len(b)-1, 3) == True), "Wrong ansser"

	print("All tests passed!")
