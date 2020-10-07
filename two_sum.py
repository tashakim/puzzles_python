import pytest
from typing import List
""" ### Task hw3.10 Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
""" TFD Steps
1. Inputs
- Integer array 'nums', and integer 'target'

2. Outputs
- Array of integer indices, res

3. Special Cases
- nums is None
- target is None
- nums == []
- target < 0
- length of nums == 1
- there are more than one pair of integers in nums, that add up to target 
	- Note: We will not consider this case, as we are given that there is exactly one solution.
- an integer in nums adds to target with itself, e.g. nums = [3, 2, 1], target = 6 => 3 + 3 = 6

4. Usual Cases
- there is only one pair of integers in nums, with distinct indices, that add up to 'target'
Example: nums = [1,2,3,4,5], target = 9 => res = [3,4]

5, 6, 7, 8: See below
"""
# 5. Function Specification, & 7. Implement Function
def two_sum(nums: List[int], target: int) -> List[int]:
	"""
	Purpose: Returns the indices of two numbers in 'nums' that add up to 'target'.

	Time Complexity: O(n), where n is length of input array nums,
	Space Complexity: O(n), where n is length of input array nums.
	"""
	if nums is None or nums == [] or len(nums) <= 1:
		raise Exception("Input array is invalid")
	if target is None or not isinstance(target, int):
		raise Exception("Input target is invalid")
	
	table = dict()

	for i, x in enumerate(nums):
		if x in table:
			return [table[x], i]
		table[target - x] = i


# 6. Implement Test Cases
def test_two_sum():
	assert two_sum([1,2,3,4,5], 9) == [3,4]
	assert two_sum([5,1,4,9], 6) == [0,1]

	assert two_sum([4,3,5], 8) == [1,2]
	assert two_sum([5,5], 10) == [0,1] 
	
	# Tests that method correctly raises Exceptions
	with pytest.raises(Exception):
		two_sum(None, 1) # Raise error when nums is None
	with pytest.raises(Exception):
		two_sum([], 24) # Raise error when nums == []
	with pytest.raises(Exception):
		two_sum([1,2,34], None) # Raise error when 'target' is None
	with pytest.raises(Exception):
		two_sum([1,2,3,4], 3.1415) # Raise error when 'target' is not an integer
	with pytest.raises(Exception):
		two_sum([0], 0) # Raise error when len(nums) <= 1
	print("All tests passed!")


test_two_sum()

# 8. Add/Improve tests as needed
# A: No additional tests needed

# END OF SOLUTION