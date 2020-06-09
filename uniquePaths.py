def uniquePaths(self, m: int, n: int) -> int:
        temp = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if(i == 0 or j == 0):
                    temp[i][j] = 1
                else:
                    temp[i][j] = temp[i-1][j] + temp[i][j-1]
        return temp[n-1][m-1]
        