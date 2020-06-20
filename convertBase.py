import math

def compareNumbers(bin, hex):
	"""Purpose: Code reuse, to check if value of a 
	binary number (passed in as string) equals the 
	hexadecimal representation of a string.
	"""
	n1 = convert(bin, 2) 
	n2 = convert(hex, 16)
	if(n1 < 0 or  n2< 0):
		return False
	return n1 == n2


def convert(n, base):
	"""Purpose: Converts the number written in base 'base'.
	"""
	val = 0
	for i in range(n):
		n = int(n)
		if(n <0 or n >= base):
			return -1
		exp = n -1 -i
		val += n*(base**exp)
	return val


if __name__ == "__main__":
	assert(compareNumbers(10, 2) == True), "Wrong answer."
	print("Test passed!")