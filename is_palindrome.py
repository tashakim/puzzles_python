def isPalindrome(s):
	"""Purpose: Given a string s, determines if it's a palindrome, 
	considering alphanumeric characters and ignoring cases.
	Note: We define an empty string as a valid palindrome.
	"""
	res = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()
	mid = len(res)//2
	for i in range(mid):
		if(res[i] != res[-i-1]):
			return False
	return True


if __name__ == "__main__":
	assert(isPalindrome("0P") == False), "Wrong answer."
	assert(isPalindrome("race a car") == False), "Wrong answer."
	assert(isPalindrome("A man, a plan, a canal: Panama") == True), "Wrong answer."
	assert(isPalindrome("") == True), "Wrong answer."

	print("All tests passed!")