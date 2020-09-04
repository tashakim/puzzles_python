class Solution():
	def numIslands(self, grid):
		"""Purpose: Return the number of islands of '1', given a
		2d graph input filled by '1' or '0'.
		"""
		if not grid: return 0
		count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					self.dfs(grid, i, j)
					count += 1
		return count

	def dfs(self, grid, i , j):
		if i <0 or j <0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
			return
		grid[i][j] = 0
		self.dfs(grid, i+1, j)
		self.dfs(grid, i-1, j)
		self.dfs(grid, i, j+1)
		self.dfs(grid, i, j-1)


if __name__ == "__main__":
	grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
	s= Solution()
	assert(s.numIslands(grid) == 1), "Wrong answer"
	print("All tests passed!")