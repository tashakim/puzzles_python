def euclid_algorithm(a,b):
	"""Purpose: Computes the greatest common divisor of two numbers, a and b.
	Note: a > b.

	"""
	while b != 0: # run while 'a' is not divisible by 'b'.
		a, b = b, a%b # by Euclid

	return a

if __name__ == "__main__":
	assert(euclid_algorithm(2,4) == 2), "Wrong value"
	assert(euclid_algorithm(12, 8) == 4), "Wrong value"
	assert(euclid_algorithm(3, 33) == 3), "Wrong value"

	print("All tests passed!")