def count_substr(s,c):
	"""Purpose: Counts the number of times a substring
	'c' appears in a string 's'.
	"""
	return sum([1 for i in range(len(s) - len(c)+1) if s[i:i+len(c)] == c])


if __name__ == "__main__":
	s = "cabacab"
	c = "cab"
	print(count_substr(s,c))