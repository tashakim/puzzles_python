def runnerup(n, arr):
	"""Purpose: Given an array of n scores, 
	returns the runner-up score.
	"""
	arr = [x for x in arr if x!=max(arr)]
	print(max(arr))
	

if __name__ == "__main__":
	runnerup(5,[2,3,6,6,5])