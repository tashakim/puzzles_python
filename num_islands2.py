class Solution:
    def numIslands(self, grid):
    """Purpose: Count the number of separated units in a 
    graph filled with '1's and '0's.
    """
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0' or visited[i][j]:
                return
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        if not grid: 
            return count
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count