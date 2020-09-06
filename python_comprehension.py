import collections

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


def filter_dupe():
	# Create a hashtable to perform a filter for duplicates
	items = ["apple", "pear", "orange", "banana", "apple",
	         "orange", "apple", "pear", "banana", "orange",
	         "apple", "kiwi", "pear", "apple", "orange"]

	filter = {}

	for item in items:
		filter.setdefault(item, int)

	print("My filter: ", filter)
	return len(items) == len(filter)


print(filter_dupe()) # False


def dupe_value_counter():
	items = ["apple", "pear", "orange", "banana", "apple",
	         "orange", "apple", "pear", "banana", "orange",
	         "apple", "kiwi", "pear", "apple", "orange"]

	filter = collections.Counter(items)
	print("Checking for duplicates... ")

	for k, v in filter.items():
		if v > 1:
			print(k, end=", ")
	print("[Complete]")

dupe_value_counter()
