def diag(a, n):
	"""Purpose: Hidden**
	Time Complexity: O(n),
	Space Complexity: O(1)
	"""
	count, res = 1, 0
	for i in range(n):
		res ^= rangeXOR(a, a + length - count)
		a += n
		count += 1
	return res


def rangeXOR(low, high):
	"""Purpose: Computes the XOR of integers between low & high.
	Time Complexity: O(1),
	Space Complexity: O(1)
	"""
	return sumXOR(low - 1)^sumXOR(high)


def sumXOR(n):
	"""Purpose: Computes the XOR of integers from 1 to n.
	Time Complexity: O(1), 
	Space Complexity: O(1)
	"""
	m = n % 4
	if m == 1: return 1
	elif m == 2: return n + 1
	elif m == 3: return 0

	return n

if __name__ == "__main__":
	assert(diag(0, 4) == 10), "Wrong"
	assert(diag(55, 3) == 10) , "Wrong"

	print("All tests passed!")