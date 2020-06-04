def myarrlessthan(p,q):
	"""Purpose: takes in two arrays p,q, and returns True if they have same size AND each element of p is less than that of q.
	Example: myarrlessthan([0,2,2], [1,3,4]) -> True
	"""
	if(len(p) != len(q)):
		return False
	else:
		for i in range(len(p)):
			if(p[i] >= q[i]):
				return False
	return True

if __name__ == "__main__":
	print(myarrlessthan([0,2,2], [1,3,4]))

	assert(myarrlessthan([1,5,3], [6,8,2]) == False), "Error"
	print("Test passed!")