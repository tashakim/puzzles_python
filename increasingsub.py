class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if(nums == []):
            return 0
        temp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if (nums[j] < nums[i] and temp[j]+1 > temp[i]):
                    temp[i] = temp[j] +1
        print(temp)
        return max(temp)