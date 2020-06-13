class InvalidInputException:
	pass

def increment(k):
	"""Purpose: Takes in a stack of 0s and 1s, respresenting 
	a binary number k, and returns a stack representing 
	binary number k+1.
	"""
	if(k == [] or k == None):
		raise InvalidInputException("Input must be valid.")

	if(k[-1] == 1):
		k.pop()
		return increment(k[:-1])

	elif(k[-1] == 0):
		k[-1] +=1


if __name__ == "__main__":
	print(increment([1]))

	assert(increment([1,0,0,0]) == [1,0,0,1]), "Wrong answer."
	assert(increment([1]) == [1,0]), "Wrong answer."
	assert(increment([0,0,1]) == [0,1,0]), "Wrong answer."
	
	print("All tests passed!")