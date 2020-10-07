import pytest

""" ### Task hw3.14 Reverse String
Write a function that reverses a string. The input string is given as an array of characters. The str type hint given in the stencil is incorrect.
Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""

""" TFD Steps
1. Inputs
- An array of characters, s

2. Outputs
- An array of characters reversed, s

3. Special Cases
- s is None
- s == []
- s contains empty character, ''
- len(s) == 1, i.e. reversed list is same as input list

4. Usual Cases
- s is an array of ascii lowercase characters, and len(s) > 1
Example: s = ['f', 'a', 'n', 't', 'a', 's', 't', 'i', 'c']
Example: s = ['1', '0', '1']

5, 6, 7, 8: See below
"""

# 5. Function Specification, & 7. Implement Function
def reverse_string(s: str) -> str:
	"""
	Purpose: Reverses an array of characters, s, in-place.

	Time Complexity: O(n), where n is length of input array,
	Space Complexity: O(1), operation is performed in-place.
	"""
	# We are given that input array only contains valid ascii characters.
	if s is None or s == []:
		raise Exception("Input array is invalid.")
	index = 0
	while index < len(s)//2:
		s[index], s[-index-1] = s[-index-1], s[index]
		index += 1
	return s


# 6. Implement Test Cases
def test_reverse_string():
	with pytest.raises(Exception): # Raise error when input is None
		reverse_string(None)
	with pytest.raises(Exception): # Raise error when array has no chars
		reverse_string([])

	assert reverse_string(['a']) == ['a'], "Single-char test failed"
	assert reverse_string(['a', 'b', 'c']) == ['c', 'b', 'a'], "Odd length test failed"
	assert reverse_string(['A', 'B', 'C', 'D']) == ['D', 'C', 'B', 'A'], "Even length test failed"

	assert reverse_string(['0', '0', '1', '2', '3', '4', '5', '6']) == ['6', '5', '4', '3', '2', '1', '0', '0'], "Longer test failed"
	assert reverse_string(['H', 'a', 'n', 'n', 'a', 'h']) == ['h', 'a', 'n', 'n', 'a', 'H'], "Upper-case test failed"

if __name__ == "__main__":
	test_reverse_string()


# 8. Add/Improve tests as needed
# A: No additional tests needed

# END OF SOLUTION
