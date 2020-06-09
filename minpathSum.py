def minPathSum(grid):
    """Purpose: Finds the path that minimizes the sum of 
    numbers in a mxn grid, that goes from top-left to bottom-right.
    """
    n = len(grid)
    m = len(grid[0])
    temp = [[0 for i in range(m)] for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if(i == 0 and j == 0):
                temp[i][j] = grid[i][j]
            elif(i == 0 and j != 0):
                temp[i][j] = grid[i][j]+temp[i][j-1]

            elif(j == 0 and i != 0):
                temp[i][j] = grid[i][j]+temp[i-1][j]
            else:
                temp[i][j] = min(grid[i][j]+temp[i-1][j], grid[i][j]+temp[i][j-1])
    return temp[n-1][m-1]


if __name__ == "__main__":
    assert(minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7), "Wrong output"
    print("Test passed!")