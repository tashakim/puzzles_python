class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Purpose: Move all occurrences of zeros to the back of array, 
        note: in-place solution. 

        Do not return anything, modify nums in-place instead.
        """
        count= nums.count(0)

        for k in range(count):
            i = nums.index(0)
            while i < len(nums) - 1:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                i += 1

        return nums

    def moveZeroes(self, nums):
        return