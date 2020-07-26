class Solution:
    def pivotIndex0(self, nums: List[int]) -> int:
    """Purpose: Returns the pivot index of this array; 
    A pivot index is the index where the sum of all numbers to 
    the left of the index equals the sum of all numbers to the right.
    
    If no such index exists, return -1.
    """
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
                
        
    def pivotIndex(self, nums):
        wholesum = sum(nums)
        for i in range(len(nums)):
            if (wholesum - nums[i])/2 == sum(nums[:i]):
                return i
        return -1