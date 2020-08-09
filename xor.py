def xor(n):
	"""Purpose: Computes the xor of all integers up to n.
	Note: uses special property of xor'ing consecutive integers.
	"""
	if n%4 == 0:
		return 0
	elif n%4 == 1:
		return 1
	elif n%4 == 2:
		return n+1
	return n


def rangeXor(left, right):
	"""Purpose: Computes the xor of all integers between 'left' and 'right'.
	Note: uses property that xor'ing twice negates the effect.
	"""
	return xor(right)^xor(left - 1)


if __name__ == "__main__":
	print(xor(3))



