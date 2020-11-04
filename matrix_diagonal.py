class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Purpose: returns the sum of matrix diagonals
        
        Time complexity: O(n), we step through matrix at most n times at each sum operation,
            where n is the length of the nxn square matrix.
        Space complexity: O(1), bc we only use one var. to keep track of resulting sum.
        """
        n = len(mat)
        res = 0
        for i in range(n): # O(n)
            res += mat[i][i]
            
        for i in range(n): # O(n)
            res += mat[i][-i-1]
            
        # if n is odd, there is one intersection at n/2
        # else if n is even, there is no intersection
        if n%2 == 1: # odd
            res -= mat[n//2][n//2]
        return res