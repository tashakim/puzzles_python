class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        Purpose: Returns the maximum total sum that the height of the buildings can be increased.
        """
        temp1 = [float('-inf')]*len(grid)
        temp2 = [float('-inf')]*len(grid[0])
        for i in range(len(grid)):
            temp1[i] = max(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] > temp2[j]:
                    temp2[j] = grid[i][j]
        count = 0 
        res = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res[i][j] = min(temp1[i], temp2[j])
                if grid[i][j] < res[i][j]:
                    count += (res[i][j]- grid[i][j])
        
        return count
        
