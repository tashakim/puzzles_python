class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        max_len = 1
        i = 0
        while i < len(nums):
            cur_max = 1

            while i+1 < len(nums) and nums[i+1] > nums[i]:
                cur_max += 1
                i += 1
            max_len = max(cur_max, max_len)
            i += 1
    
        return max_len

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
    
        return max(dp)