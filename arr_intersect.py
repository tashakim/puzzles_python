from typing import List
from collections import Counter
import pytest
""" ### Task hw3.11 Array Intersection
Given two arrays, return the intersection of these two arrays (there could be duplicate numbers).
"""
""" TFD Steps
1. Inputs
- String s, and string t

2. Outputs
- Boolean, True or False

3. Special Cases
- nums1 is None or nums2 is None
- nums1 == [], or nums2 == []
- nums1 contains repeated instances of a char in nums2
- vice versa, nums2 contains repeated instances of a char in nums1

4. Usual Cases
- nums1, nums2 are int arrays, each with length >= 1
Example: nums1 = [1, 2, 2, 3], nums2 = [2, 3, 4]

5, 6, 7, 8: See below
"""
# 5. Function Specification, & 7. Implement Function
def array_intersection(nums1: List[int], nums2: List[int]) -> List[int]:
	"""
	Purpose: Returns a list of common elements from input arrays.

	Time Complexity: O(max(n, m)), where n is length nums1, m is length of nums2
	Space Complexity: O(n), where n is length of nums2
	"""
	if nums1 is None or nums2 is None:
		raise Exception("Input array(s) is invalid")

	res = []
	table = Counter(nums2)
	for num in nums1:
		if num in table and table[num] >= 1:
			res.append(num)
			table[num] -= 1
	return res


# 6. Implement Test Cases
def test_array_intersection():
	assert array_intersection([1], [11]) == []
	assert array_intersection([1], [1]) == [1]
	assert array_intersection([1], [1, 1]) == [1]
	assert array_intersection([1, 1, 1], [1, 1]) == [1,1]

	assert array_intersection([1,2,2,1], [2,2]) == [2,2]
	assert array_intersection([4,9,5],[9,4,9,8,4]) == [4,9]
	assert array_intersection([1,3,3,0], [3]) == [3]

	with pytest.raises(Exception):
		array_intersection(None, None) # Raises error when input array is None

	print("All tests passed!")


test_array_intersection()

# 8. Add/Improve tests as needed
# A: No additional tests needed

# END OF SOLUTION
