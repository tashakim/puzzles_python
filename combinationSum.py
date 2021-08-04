class Solution:
    def combinationSum(self, candidates, target):
        """
        Purpose: Utilizes Depth-first-search to return a list of all unique combinations
        of candidates where chosen numbers sum to target.

        Combinations can be returned in any order, and 
        the same number may be chosen from candidates an unlimited no. of times.
        
        """
        def traverse(arr, target, path):
            if target < 0: return 
            
            if target == 0:
                self.res.append(path)
                return 
            
            for i in range(len(arr)):
                traverse(arr[i:], target - arr[i], path + [arr[i]])
                
        self.res = []
        traverse(candidates, target, [])
        return self.res

    