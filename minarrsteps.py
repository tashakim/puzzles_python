def minsteps(arr):
	"""Purpose:
	Example: minsteps([3]) -> 0
	minsteps([1,0]) -> 1
	minsteps([3,1,2,0,8]) -> 2
	"""
	temp = [0]*len(arr)
	for i in range(1, len(arr)):
		for j in range(i):
			if(arr[j] >= i-j):
				if(temp[j] == 0):
					temp[i] = 1
				if(temp[i] == 0):
					temp[i] = temp[j]+1
				elif(temp[i] > temp[j]+1):
					temp[i] = temp[j] +1
	return temp[-1]


if __name__ == "__main__":
	assert(minsteps([3,1,2,0,8]) == 2), "Wrong answer" 
	assert(minsteps([1,0]) == 1), "Wrong answer"
	assert(minsteps([1,0,0,5]) == 0), "Wrong answer"

	print("All tests passed!")