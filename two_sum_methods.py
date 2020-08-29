class Solution:
    def twoSum0(self, nums: List[int], target: int) -> List[int]:
    """Purpose: Hashing
    """
        my_hash = dict()
        for i,x in enumerate(nums):
            k = target - nums[i]
            if nums[i] not in my_hash:
                my_hash[k] = i
            else:
                return [i, my_hash[nums[i]]]

    def twoSum(self, nums, target):
    """Purpose: Two pointers
    """
        p1, p2 = 0, len(nums)-1
        while p1 < p2:
            p_sum = nums[p1] + nums[p2]
            if p_sum == target:
                return [p1, p2]
            elif p_sum < target:
                p1 += 1
            else:
                p2 -= 1
            