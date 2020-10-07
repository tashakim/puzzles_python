from typing import List
import pytest
""" ### Task hw3.7 Move Zeroes
Given an array, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""
""" TFD Steps
1. Inputs
- 

2. Outputs
- 

3. Special Cases
- 

4. Usual Cases
- 
Example: 
Example: 

5, 6, 7, 8: See below
"""
# 5. Function Specification, & 7. Implement Function
def move_zeroes(nums: List[int]) -> None:
	"""Purpose: Returns a 

	Time Complexity: 
	Space Complexity: O(1), modifies input array in-place.
	"""
	for i, x in enumerate(nums):
		if x == 0:
			shift_to_back(i, nums)
	return nums

def shift_to_back(index, arr):
	"""
	Purpose: Helper method that shifts item at index 'index' to the back of arr.
	Time Complexity: O(n), where n is length of input arr,
	Space Complexity: O(1), does not use additional space.
	"""
	while index < len(arr)-1:
		arr[index], arr[index+1] = arr[index+1], arr[index]
		index += 1
	return arr


# 6. Implement Test Cases
def test_move_zeroes():
	assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]


test_move_zeroes()

# 8. Add/Improve tests as needed
# A: No additional tests needed

# END OF SOLUTION