import pytest
from typing import List
""" ### Task hw3.9 Delete N-th
Given a list lst and a number N, create a new list that contains each number of the list at most N times without reordering.
"""
""" TFD Steps
1. Inputs
- An array array, and number N

2. Outputs
- An array, res 

3. Special Cases
- array is None
- len(array) == 0
- N == 0, no numbers should be printed
- N < 0, should raise Exception

4. Usual Cases
- Input array is list of numbers, len(array) >= 1, and N >= 1
Example: array = [1,2,3], N = 1 	=> [1,2,3]
Example: array = [0,0,0,0], N = 3 	=> [0,0,0]

5, 6, 7, 8: See below
"""
# 5. Function Specification, & 7. Implement Function
def delete_nth(array: List[int], n: int) -> List[int]:
	"""
	Purpose: Returns a new list that contains each number of array at most N times, without reordering.

	Time Complexity: O(k), where k is length of input array,
	Space Complexity: O(k), where k is length of input array.
	"""
	if array is None:
		raise Exception("Input array is invalid")
	if n < 0:
		raise Exception("Input n is invalid")

	table, res = dict(), []
	for x in array:
		if x not in table and n != 0:
			table[x] = 1
			res.append(x)
		elif x in table:
			if table[x] < n:
				table[x] += 1
				res.append(x)
	return res


# 6. Implement Test Cases
def test_delete_nth():
	assert delete_nth([1,2,3,1,2,1,2,3], 2) == [1,2,3,1,2,3]
	assert delete_nth([0,0,0,0,0,0], 5) == [0,0,0,0,0]
	assert delete_nth([1,1,2,2,1,2,1,2], 1) == [1, 2] 

	assert delete_nth([10, 5, 3, 3, 6, 1], 0) == []
	assert delete_nth([], 1) == []

	with pytest.raises(Exception):
		delete_nth(None, 2)
	with pytest.raises(Exception):
		delete_nth([0], -1)
	print("All tests passed!")


test_delete_nth()

# 8. Add/Improve tests as needed
# A: No additional tests needed

# END OF SOLUTION