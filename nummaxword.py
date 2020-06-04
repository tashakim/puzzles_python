def max_word(s):
	"""Purpose: takes in a string, and returns the no. of occurrences of most common word in string.
	Example: max_word("Hello world!") -> 1
	max_word("the quick the fox") -> 2
	"""
	l = s.split()
	mydict = {}
	for word in l:
		mydict[word] = l.count(word)
	return mydict[max(mydict)]


if __name__ == "__main__":
	
	assert(max_word("Hello world!") == 1), "Wrong answer"
	assert(max_word("the quick the fox") == 2), "Wrong answer"
	print("All tests passed!")