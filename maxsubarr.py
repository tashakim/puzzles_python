"""These are sample solutions for finding the max subarray,
from a given list of integers. 
Task: Evaluate the Runtime Complexity, and worst-case Space
Complexity of the following methods.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	"""Purpose: Returns the maximum subarray 
    	from a given array of integers. My SOL.
    	"""
        sums = nums
        for i in range(1,len(nums)):
            if sums[i-1] + nums[i] > nums[i]:
                sums[i] = sums[i-1] + nums[i]
        
        return max(sums)

    def maxSubArray2(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    def maxSubArray3(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        n = len(nums)
        
        for i in range(1,n):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(current_sum, max_sum)
        return max_sum

    def maxSubArray4(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curMax = 0
        for i in range(len(nums)):
            curMax = max(nums[i], curMax + nums[i])
            max_sum = max(curMax,max_sum)
        return max_sum

    def maxSubArray5(self, nums: List[int]) -> int:
        curr_ = -float('inf')
        max_sum = -float('inf')
        for num in nums:
            if curr_ < 0:
                curr_ = num
            else:
                curr_ += num
            max_sum = max(max_sum, curr_)
        return max_sum        


if __name__ == "__main__":
	s = Solution()
	s.maxSubArray([1,4,5,1,-3,-5,0,4,-3])