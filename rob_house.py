class Solution:
    def rob(self, nums: List[int]) -> int:
    """Purpose: Assures no two adjacent houses are robbed.
    Utilizes dynamic programming.
    """
        if len(nums) == 0: 
            return 0
        elif len(nums) == 1: 
            return nums[0]
        
        dp = [0]*len(nums)
        max_sum = 0
        dp[0], dp[1] = nums[0], nums[1] # initialize first elements
        
        for i in range(2, len(nums)):
            for j in range(i-1):
                if nums[i] + dp[j] > dp[i]:
                    dp[i] = nums[i] + dp[j]
                    
        return max(dp)


if __name__ == "__main__":
    assert(Solution().rob([1,2,3,1]) == 4), "Wrong answer"
    assert(Solution().rob([2,7,9,3,1]) == 12), "Wrong answer"

    print("All tests passed!")