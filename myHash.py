# needs work

def isPrime(n):
	"""Purpose: This method checks whether n is prime.
	Example: isPrime(3) -> True
	isPrime(4) -> False
	"""
	for i in range(2, int(num//2)+1):
		if n%i == 0:
			return False
	return True

def smallestPrime(n):
	"""Purpose: Returns the smallest prime number
	greater than n.
	Example: smallestPrime(4) -> 5
	smallestPrime(8) -> 11
	"""
	while not isPrime(n):
		n +=1
	return n

class HashSet():
	"""Purpose: Simple python implementation of a hash set.
	"""
	def __init__(self, size = 256, key_length = 3):

		# check  invalid  inputs

		self._expSize = size
		self._keyLength = key_length

		#  first, find the smallest prime greater than  
		# the expected size.
		if(self._expSize <= 256):
			p = smallestPrime(256)
		else:
			p = smallestPrime(self._expSize)

		# underlying array forthe hash set.
		self._hashSet = [ [] for i in range(p)]
		self._hashSize = 0

		# Initialize  other instance  variables.




