class Error(Exception):
	pass
class InvalidInputException:
	pass

def compareTriplets(arr1, arr2):
	"""Purpose:
	"""
	if(len(arr1) == len(arr2)):
		raise Error("Array lengths must be the same.")

	if(arr1 == [] or arr1 == None or arr2 == [] or arr2 == None):
		raise InvalidInputException("Arrays are invalid.")

	result = [0,0]
	for i in range(len(arr1)):
		if(arr1[i]>arr2[i]):
			result[0] +=1 
		elif(arr1[i]<arr2[i]):
			result[1] +=1

	return result


if __name__ == "__main__":
	assert(compareTriplets([1,2,3],[2,3,4]) == [0,3]), "Wrong answer"
	assert(compareTriplets([0,0,3,0,1,5], [1,1,1,2,2,2]) == [2,4]), "Wrong answer"
	print("All tests passed!")