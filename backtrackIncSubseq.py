class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        Purpose: Returns all different possible increasing subsequences of 
        a given array with at least two elements. 

        Note: Answer can be returned in any order.
        """
        def traverse(arr, start, path, seen):
            if len(path) >=2 and path not in self.res and path == sorted(path):
                self.res.append(path[:])
            for i in range(start, len(arr)):
                if i not in seen:
                    path.append(arr[i])
                    seen.add(i)
                    traverse(arr, i+1, path, seen)
                    
                    path.pop()
                    seen.remove(i)

        self.res = []
        traverse(nums, 0, [], set())
        return self.res


    def findSubsequences1(self, nums):
        """
        Improved solution.
        """
        def traverse(arr, start, path):
            if len(path) >= 2 and path not in self.res and path == sorted(path):
                self.res.append(path[:])

            for i in range(start, len(arr)):
                path.append(arr[i])
                traverse(arr, i+1, path)
                path.pop()

        self.res = []
        traverse(nums, 0, [])
        return self.res

    def addToTarget(self, nums, target):
        """
        Purpose: Finds all subsequences whose elements add up to target.
        """
        def backtrack(arr, start, path):
            # stop condition
            if sum(path) == target:
                self.res.append(path[:])

            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(arr, start+1, path)
                path.pop()

            return
        
        self.res = []
        backtrack(nums, 0, [])
        return self.res