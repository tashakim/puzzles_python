def runnerupScore(n, arr):
	"""Purpose: Given an array of n scores, 
	returns the runner-up score.
	"""
	arr = [x for x in arr if x!=max(arr)]

	return max(arr)


def bestScore(n,arr):
	"""Purpose: Returns the best score from input array.
	"""
	return max(arr)

if __name__ == "__main__":
	runnerupScore(5,[2,3,6,6,0])

	assert(bestScore(5,[2,3,6,6,5]) == 6), "Wrong answer"
	assert(runnerupScore(5,[2,3,6,6,5]) == 5), "Wrong answer"
	print("All tests passed!")

