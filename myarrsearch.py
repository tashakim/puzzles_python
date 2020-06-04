def arraysearch(num, arr):
	"""Purpose: takes an int and array, and returns True if int is in array.
	Example: arraysearch(3, [1,3,4] -> True)
	"""
	for item in arr:
		if(num == item):
			return True
	return False

if __name__ == "__main__":
	print(arraysearch(2, [1,2,3]))
	print(arraysearch(2, [1,3,4]))