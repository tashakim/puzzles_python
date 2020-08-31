class Solution:
    def firstMissingPositive0(self, nums: List[int]) -> int:
        # naive solution
        nums.sort()
        i = 1
        while i > 0:
            if i not in nums:
                return i
            i += 1
        return i
    
    def firstMissingPositive1(self, nums):
        i = 1
        while i >= 1: # O(m), where m is first missing positive. m <= n+1
            if i not in nums: # O(n), where n is no. of items in array
                return i
            i += 1
        # => Total time complexity: O(n*m)
        
    def firstMissingPositive(self, nums):
        if 1 not in nums:
            return 1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        for i,x in enumerate(nums):
            if nums[abs(x)-1] > 0:
                nums[abs(x)-1] *= -1
        i = 0
        while i < len(nums) and nums[i] < 0:
            i += 1
        return i + 1