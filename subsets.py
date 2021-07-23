import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Purpose: Given an int array of unique items, returns all possible subsets.

        Note: This is equivalent to the power set.
        """
        res = []
        for i in range(len(nums)+1):
            res.extend([list(x) for x in itertools.combinations(nums, i)])

        return res


    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """
        Cascading solution:
        Starting from an empty subset in resulting list, takes new item at each step 
        to generate new subsets from existing ones.
        """
        res = [[]]
        for i in nums:
            res += [x + [i] for x in res]
        
        return res


    def subsets3(self, nums):
        """
        Backtracking solution
        """
        def backtrack(first=0, cur=[]):
            if len(cur) == k:  
                output.append(cur[:])
                return

            for i in range(first, n):
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()
        
        res = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return res