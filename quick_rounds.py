import collections

def reverse(n):
	"""Purpose: given an integer n, returns the integer with reversed digits.
	"""
	n = str(n)
	if n[0] == '-': # case: n < 0
		n = n[1:]
	return int(n[::-1])

def avg_length(s):
	"""Purpose: given a sentence s, returns the average word length.
	"""
	for x in ".,?!;:":
		s = s.replace(x, "")
	lengths = [len(word) for word in s.split(" ")]

	return sum(lengths)/len(lengths)



def add_str(num1, num2):
	"""Purpose: given two non-negative integers num1 and num2 represented as 
	a string, return the sum of the two (not using int() function).
	"""
	return str(eval(num1) + eval(num2))

def first_unique(s):
	"""Purpose: given a string, find fist non-repeating char in it and return its index.
	"""
	myset = set()
	for i in range(len(s)):
		if s[i] in myset:
			return i
		else:
			myset.add(s[i])
	return -1

	"""OR:
	count = collections.Counter(s)
	for i, c in enumerate(s):
		if count[c] == 1:
			return i
	return -1
	"""

def palindrome(s):
	"""Purpose: given a non-empty string s, check if s is a valid palindrome 
	after deleting at most one character.
	"""
	mid = len(s)//2
	print(collections.Counter(s[:mid]))
	print(collections.Counter(s[mid+1:]))
	if abs(sum(collections.Counter(s[:mid]).keys()) - sum(collections.Counter(s[mid+1:]).keys()) ) != 1:
		return False


if __name__ == "__main__":
	print(reverse(12345))
	print(avg_length("Hi all, my name is Tash... and I am originally from South Korea."))
	print(add_str('5', '40'))
	print(first_unique("iron man is on the rise"))
	palindrome('abcdabc')

