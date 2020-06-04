def conundrum(arr):
	"""Purpose: returns maximum profits given an array of profits on each day.
	Example: conundrum([-1,2,7,-8,13,-2]) -> 194
	"""
	temp = [0]*len(arr)
	if(temp[0] + arr[0] > temp[0]):
		temp[0] += arr[0]
	for i in range(1, len(arr)):
		if(temp[i] + arr[i] > temp[i]):
			temp[i] = arr[i] + temp[i-1]
			print(arr)
			print(temp)

	return temp


if __name__ == "__main__":
	print(conundrum([-1,2,7,-8,13,-2]))