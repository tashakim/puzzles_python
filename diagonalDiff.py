class InvalidInputException:
	pass

def diagonalDiff(arr):
	"""Purpose: Calculates the absolute difference
	between sums of the diagonals, of a square matrix.
	"""
	if(len(arr) != len(arr[0])):
		raise InvalidInputException("Input is invalid.")

	sum1, sum2 = 0, 0
	for i in range(len(arr)):
		sum1 += arr[i][i]
	for i in range(len(arr)):
		sum2 += arr[i][-i-1]
	return abs(sum1 - sum2)


if __name__ == "__main__":
	a = [[11,2,4], [4,5,6], [10,8,-12]]
	assert(diagonalDiff(a) == 15), "Wrong answer"

	print("Test passed!")