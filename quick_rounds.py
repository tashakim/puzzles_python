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
	for i in range(len(s)):
		if s[i] != s[-1-i]:
			return s[:i] == s[i+1:]
	return s == s[::-1]


def monotonic(nums):
	"""Purpose: given an array of integers, determine whether the array is monotonic.
	"""
	# return nums.sort() == nums 
	# BETTER:
	return all(nums[i] <= nums[i+1] for i in range(len(nums) -1)) or all(nums[i] >= nums[i+1] for i in range(len(nums) -1))

def move_zeros(nums):
	"""Purpose: given an array of integers, move all zeros to the end, while maintaining
	order of elements.
	"""
	for i in range(len(nums)):
		if nums[i] == 0:
			nums.append(nums[i])
			nums.pop(i)
	return nums


def fill_blank(arr):
	"""Purpose: given an array, fill the None values with most-recent non-None value in array.
	"""
	recent = float('inf')
	for i in range(len(arr)):
		if arr[i] != None:
			recent = arr[i]
		else:
			arr[i] = recent
	return arr

def match_mismatch(s1, s2):
	"""Purpose: given two sentences, return an array with words in common,
	and another array with words NOT in common.
	"""
	s1, s2 = set(s1.split(" ")), set(s2.split(" "))
	match, mismatch = [], []

	for word in s1:
		if word in s2:
			match.append(word)
		else:
			mismatch.append(word)
	return match, mismatch

def prime(n):
	"""Purpose: return the set of prime numbers less than n.
	"""
	isprime = []
	for i in range(2,n):
		if all(i%x != 0 for x in range(2, i)):
			isprime.append(i)
	return isprime


if __name__ == "__main__":
	print(reverse(12345))
	print(avg_length("Hi all, my name is Tash... and I am originally from South Korea."))
	print(add_str('5', '40'))
	print(first_unique("iron man is on the rise"), end = "\n\n")
	
	print(palindrome('radkdar'))
	print(palindrome('abcdabc'), end = "\n\n")

	print(monotonic([1,2,4,5]))
	print(move_zeros([1,0,2,3,4,0,5]))
	print(fill_blank([1,None,2,None, 3,4, None]))
	print(match_mismatch("one two three four", "one three four five"), end = "\n\n")
	print(prime(10))


	print("All tests passed!")

