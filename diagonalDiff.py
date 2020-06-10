def diagonalDiff(arr):
	"""Purpose:
	"""
	sum1 = 0
	sum2 = 0
	for i in range(len(arr)):
		sum1 += arr[i][i]
	for i in range(len(arr)):
		sum2 += arr[i][-i-1]
	return abs(sum1 - sum2)

if __name__ == "__main__":
	a = [[1,2,3], [4,5,6], [7,8,9]]
	diagonalDiff(a)