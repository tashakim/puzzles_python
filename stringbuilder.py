from array import array

def stringBuilder(strings):
	"""Purpose: Concatenates a list of strings.

	# Method 1: Naive appending. 
	Each time word is iterated, new string is created.
	Runtime: O(xn^2).
	"""
	result = ""
	for word in strings:
		result += word
	return result

	# Method 2: Use character arrays. 
	

def stringlistBuilder(strings):
	# Method 3: Build list of strings -> join into string once.
	# Runtime: O(n).
	return "".join(strings)


if __name__ == "__main__":
	l = ["result", "is", "a", "string"]
	print(stringBuilder(l))
	print(stringlistBuilder(l))
