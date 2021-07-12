class Solution:
    def uniqueBinTree(self, n: int):
        """
        Purpose: Returns the number of structurally unique BST (binary search trees) that has 
        exactly n nodes of unique values from 1 to n.
        Time complexity: O(n*2), 
        Space complexity: O(n)
        """
        dp = [None] * (n+1)
        dp[0] = 1

        def recurse(n):
            if dp[n]: return dp[n]

            res = 0
            for i in range(1, n+1):
                res += (dp[i-1] * dp[n-i])
            dp[n] = res
            return res
        
        return recurse(n)