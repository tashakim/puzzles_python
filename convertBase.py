def compareNumbers(bin, hex):
	"""Purpose: Code reuse, to check if value of a 
	binary number (passed in as string) equals the 
	hexadecimal representation of a string.
	"""
	if (convert(bin, 2) <0 or convert(hex, 16) <0):
		return False
	return True


def convert(n, base):
	"""Purpose: Converts the number written in base 'base'.
	"""
	for i in range(len(n)):
		n = int(n)
		if(n <0 or n >= base):
			return -1
		exp = len(n) -1 -i
		val += n*Math.pow(base, exp)
	return val


if __name__ == "__main__":
	assert(compareNumbers(10, 2) == True), "Wrong number."
	print("Test passed!")