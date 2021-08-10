class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        Purpose: Returns the smallest possible length of a contiguous subarray of nums,
        that has the same degree as nums.

        """
        left, right, count = dict(), dict(), dict()
        
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1 # O(n) way of counting dupe elms.
            # Instead of: 
        # for x in nums: count[x] = nums.count(x)

        res = len(nums)
        degree = max(count.values()) # set degree of elm counts.
        # Instead of: [k for k,v in count.items() if v == max_val][0]
        
        for x in count:
            if count[x] == degree:
                res = min(res, right[x] -left[x] + 1)

        return res