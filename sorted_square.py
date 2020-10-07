import pytest
from typing import List
""" ### Task hw3.8 Sorted Squares
Given an array of integers nums sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

"""
""" TFD Steps
1. Inputs
- An integer array, nums

2. Outputs
- An integer array

3. Special Cases
- nums is None
- len(nums) == 0

4. Usual Cases
- nums is a valid integer array, len(nums) >= 1, sorted in non-descending order.
Example: nums = [-5, 0, 1, 11]
Example: nums = [-3, -2, -1, 1, 2, 3]

5, 6, 7, 8: See below
"""
# 5. Function Specification, & 7. Implement Function
def sorted_squares(nums: List[int]) -> List[int]:
	"""
	Purpose: Returns array of squares of integers in nums, in non-decreasing order.

	Time Complexity: O(n), where n is length of nums,
		Instead of taking O(n*log(n)) to merge, we step through items of array only ONCE when merging.
	Space Complexity: O(n), where n is length of nums.
		We store all items of input array, divide by sign then merge.
	"""
	if nums is None or len(nums) == 0:
		raise Exception("Input array is invalid")

	neg, pos = [], []
	for x in nums: # Loop through input array, divide positive vs. negative => O(n)
		if x < 0:
			neg.append(x**2)
		else:
			pos.append(x**2)

	res, i, j = [], -1, 0

	# Loop through negative array, merge two arrays => O(n), n is len(nums)
	# Note this is equal to O(n + m), where n = len(neg), m = len(pos)
	while i >= -len(neg):
		if neg[i] <= pos[j]:
			res.append(neg[i])
			i -= 1
		else:
			res.append(pos[j])
			j += 1
	res.extend(pos[j:])
	return res


# 6. Implement Test Cases
def test_sorted_squares():
	assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
	assert sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

	with pytest.raises(Exception):
		sorted_squares(None)
	with pytest.raises(Exception):
		sorted_squares([])
	print("All tests passed!")

	
test_sorted_squares()

# 8. Add/Improve tests as needed
# A: No additional tests needed

# END OF SOLUTION