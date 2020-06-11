class InvalidArrayException:
	pass

def hourglass(arr):
	"""Purpose: Prints the maximum sum of hourglass 
	values.
	"""
	if(len(arr) < 0 or len(arr[0]) < 0):
		raise InvalidArrayException("Input array is invalid")

	sum = []
	for i in range(len(arr[0])-2):
		for j in range(len(arr)-2):
			# sum.append(arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j+1] +arr[i][j+2] + arr[i+1][j+2] + arr[i+2][j+2])
			sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
	return max(sum)


if __name__ == "__main__":
	arr = [[1,1,1,0,0,0], [0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
	assert(hourglass(arr) == 19), "Wrong answer"
	print("Test passed!")