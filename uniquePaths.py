def uniquePaths(m: int, n: int) -> int:
	"""Purpose: A robot located at the top-left corner
	of a mxn grid can either move down or right.
	How many unique paths are there?
	"""
        temp = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if(i == 0 or j == 0):
                    temp[i][j] = 1
                else:
                    temp[i][j] = temp[i-1][j] + temp[i][j-1]
        return temp[n-1][m-1]

if __name__ == "__main__":
	assert(uniquePaths(1,1) == 1), "Wrong  answer "
	assert(uniquePaths(2,2) == 2), "Wrong answer"
	assert(uniquePaths(9,3) == 45), "Wrong answer"

	print("All tests passed!")