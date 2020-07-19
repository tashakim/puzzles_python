class Solution:
	"""Purpose: Removes duplicates from a sorted array.
	T.C: This solution beats 98.14% of python3 online submissions.
	Memory usage: 15.6 MB
	S.C: O(1). 
	"""
    def removeDuplicates(self, nums: List[int]) -> int:
        el, count = float('inf'), 0
        for i in range(len(nums)):
            if el != nums[i]:
                count += 1
                el = nums[i]
                nums[count-1] = el
        return count
    
