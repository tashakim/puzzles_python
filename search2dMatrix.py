class Solution:
    def searchMatrix(self, matrix, target):
        """
        Purpose: searches 2D matrix, and returns True if target is found.
        
        Time complexity: O(n*n)
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == target:
                    return True
        
        return False


    def searchMatrix1(self, matrix, target):
        """
        Purpose: searches 2D matrix, and returns True if target is found.

        Time complexity: O(n*n)
        """
        res = []
        for x in matrix:
            res.extend(x)

        return target in res


    def searchMatrix2(self, matrix, target):
        """
        Purpose: Binary searches 2D matrix, and returns True if target is found.
        
        Time complexity: O(log(n))
        """
        res = []
        for x in matrix:
            res.extend(x)
        
        res.sort()
        left, right = 0, len(res)-1

        while left <= right:
            mid = (left + right)//2

            if target == res[mid]:
                return True
            elif target < res[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False 