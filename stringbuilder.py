def stringBuilder(my_list):
	"""Purpose: Concatenates a list of strings.
	Method 1: Runtime complexity of O(xn^2),
	Method 2: Runtime complexity of O(n)
	"""
	result = ""
	for word in my_list:
		result = result + word
	return result


if __name__ == "__main__":
	l = ["result", "is", "a", "string"]
	print(stringBuilder(l))