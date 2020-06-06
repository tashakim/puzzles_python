def in_placeBinSearch(arr, high, low, x):
	"""Purpose:
	Runtime: 
	"""
	if(low == high):
		return arr[low] == x

	mid = (low + high)//2
	if(x == arr[mid]):
		return True
	if(x > arr[mid]):
		return in_placeBinSearch(arr, mid+1)
	if(x < arr[mid]):
		return in_placeBinSearch()



if __name__  == "__main__":
	a  = [1,2,3,4,5]
	in_placeBinSearch(a, )