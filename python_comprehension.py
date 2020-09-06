def check_sorted(data):
	"""Purpose: Brute force sorts items in input data.
	Time complexity: O(n)

	Write this method using python comprehension.
	"""

	"""
	for i in range(len(data)-1):
		if data[i] > data[i+1]:
			return False
	return True
	"""

	return all(data[i] <= data[i+1] for i in range(len(data)-1)) # One-liner!


print(check_sorted([1,3,5,6,8,100])) # True
print(check_sorted([3,5,6,8,1,100])) # False

print("Check!")