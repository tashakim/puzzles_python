class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Purpose: Given an m x n integer matrix, sets its entire row and column to 0's if
        element is 0. Returns the matrix.

        """
        copied = matrix.copy()
        rows = set()
        columns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        
        for i in range(len(copied)):
            for j in range(len(copied[0])):
                if i in rows or j in columns:
                    copied[i][j] = 0
                else:
                    copied[i][j] = matrix[i][j]
                    
        return copied


    def setZeroes1(self, matrix):
        """
        Does not return anything, modifies matrix in-place instead.
        """
        self.matrix = matrix
        def setZeroes(i, j):
            for x in range(len(matrix[0])):
                self.matrix[i][x] = 0
            for y in range(len(matrix)):
                self.matrix[y][j] = 0
                
        seen = set()            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.matrix[i][j] == 0:
                    seen.add((i, j ))
                    
        for item in seen:
            setZeroes(item[0], item[1])
