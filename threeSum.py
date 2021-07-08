class Solution:
    def threeSum(nums):
        # Purpose: Returns all triplets [nums[i], nums[j], nums[k]], where 
        # i != j != k, and nums[i] + nums[j] + nums[k] == 0

        self.res = []

        def twoSum(nums, i):
            # Purpose: 
            seen = set() # Keeps track of all j-th element of distinct triplet
            j = i + 1
            while j < len(nums):
                req = - (nums[i] + nums[j])
                if req in seen:
                    self.res.append([nums[i], nums[j], req])
                    while j + 1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1

                seen.add(nums[j])
                j += 1
        
        nums.sort() # log(n) time complexity to sort.
        for i in range(len(nums)):
            if nums[i] > 0: # first element always negative (or zero).
                break
            if i == 0 or nums[i-1] != nums[i]:
                twoSum(nums, i)

        return self.res