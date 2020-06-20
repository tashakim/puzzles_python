import math

def compareNumbers(bin, hex):
	"""Purpose: Code reuse, to check if value of a 
	binary number (passed in as string) equals the 
	hexadecimal representation of a string.
	"""
	n1 = toDigit(convert(bin, 2))
	n2 = toDigit(convert(hex, 16))
	if(n1 < 0 or n2 < 0):
		return False
	return n1 == n2


def convert(n, base):
	"""Purpose: Converts the number written in base 'base'.
	"""
	if(n == 0):
		return [0]
	res = []
	while(n):
		res.append(int(n%base))
		n //= base
	return res[::-1]


def toDigit(list):
	list = [str(x) for x in list]
	return int("".join(list))


if __name__ == "__main__":
	print(toDigit(convert(2, 2)))
	print(toDigit(convert(2, 16)))

	print(toDigit(convert(4, 2)))
	print(toDigit(convert(160, 16)), "\n")

	assert(compareNumbers(4, 160) == True), "Wrong answer."
	assert(compareNumbers(111, 3) == False), "Wrong answer."

	print("All tests passed!")