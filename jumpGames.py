class Solution:
    def canJump(self, nums):
        """
        Purpose: Given an integer array `nums`, each elm. of array represents max. jump length from that position.
        Returns whether you can reach the last index.

        """
        m = 0 
        for i, x in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + x)

        return True


    def minJumps(self, nums: List[int]) -> int:
        """
        Purpose: Returns the min. no. of jumps you need to reach the last index,
        given the rules above.

        """
        count = 0
        end_range = 0
        m = 0

        for i,x in enumerate(nums[:-1]):
            m = max(m, i + x)
            if i == end_range: # Greedy approach
                count += 1
                end_range = m
                    
        return count