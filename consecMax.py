def findConsecutiveMax(array):
	maxNo = 1
	newMax = 1
	previous = None
	for element in array:
		if element == previous:
			newMax+=1
			if newMax > maxNo:
				maxNo = newMax
		else:
			previous = element
			newMax = 1
	return maxNo




if __name__ == "__main__" :
	array = [1,2,3,3,4,5,3,7,7,7,3]
	array2 = [1,2,2,2,2,3]
	array3 = [0,0,1,2,3]

	print(findConsecutiveMax(array))
	print(findConsecutiveMax(array2))
	print(findConsecutiveMax(array3))

	assert findConsecutiveMax([0,1,0,1]) == 1, "False output"
	assert findConsecutiveMax([1,2,3,3]) == 2, "False output"
