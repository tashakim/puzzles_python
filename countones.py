def countone(n):
	""" 
	Input: integer, decimal representation
	Output: integer 
	Purpose: counts the number of 1's in binary representatino of input
	"""
	bin = []
	binaryRep(n, bin)
	count = bin.count(1)
	return count



def binaryRep(n, bin) :
	""" Helper method turns decimal digits to 
	binary digits.
	"""
	if n>1:
		binaryRep(n//2, bin)
	bin.append(n%2)
	return bin



if __name__ == "__main__":
	for i in range(0, 10):
		print("The number of 1's in binary representation of ", i, " is : ", countone(i))
