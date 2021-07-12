class Solution:
    def searchRange(self, nums: List[int], target: int):
        """
        Purpose: Returns the starting and ending position [start, end] of a 
        given target value in a sorted array 'nums'.

        Time complexity: O(log(n))
        """
        def bisect_search(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1

        p = bisect_search(nums, target)
        if p == -1: return [-1, -1]

        start = end = p
        while start - 1 > 0 and nums[start-1] == nums[p]:
            start -= 1
        while end + 1 < len(nums) and nums[end+1] == nums[p]:
            end += 1

        return [start, end]