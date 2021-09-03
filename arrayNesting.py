class Solution:
    def arrayNesting1(self, nums: List[int]) -> int:

        """
        Purpose:  Build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

        - The first element in s[k] starts with the selection of the element nums[k] of index = k.
        - The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
        - We stop adding right before a duplicate element occurs in s[k].
        """
        visited = [0]*len(nums)
        max_depth = 0
        for i in nums:
            depth = 0
            while not visited[i]:
                depth += 1
                visited[i] = 1
                i = nums[i]      
            max_depth = max(max_depth, depth)
        return max_depth
                

    def arrayNesting(self, nums: List[int]) -> int:
        """
        Purpose: Uses graph traversal to solve the above problem.
        """
        def traverse(i, nums, count):
            if self.visited[i]:
                self.res = max(self.res, count)
                return
            self.visited[i] = True
            traverse(nums[i], nums, count+1)
        
        self.res = 0
        self.visited = [False] * len(nums)
        for i in nums:
            traverse(i, nums, 0)
            
        return self.res

    