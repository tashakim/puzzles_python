class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Purpose: Returns boolean indicating whether input `word` exists in the 2x2 grid board.

        Input: [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
        Output: "ABCESEEEFS"
        
        """
        self.bool = False

        def traverse(i, j, k, seen):
            if board[i][j] != word[k]: return
            if k == len(word)-1 and word[k] == board[i][j]: 
                self.bool = True 
                return

            seen.add((i, j))

            if i-1 >= 0 and board[i-1][j] == word[k+1] and (i-1,j) not in seen: # up
                temp = seen.copy()
                traverse(i-1, j, k+1, temp)
                
            if i+1 < len(board) and board[i+1][j] == word[k+1] and (i+1,j) not in seen: # down
                temp = seen.copy()
                traverse(i+1, j, k+1, temp)
                
            if j-1 >= 0 and board[i][j-1] == word[k+1] and (i, j-1) not in seen: # left
                temp = seen.copy()
                traverse(i, j-1, k+1, temp)
                
            if j+1 < len(board[0]) and board[i][j+1] == word[k+1] and (i, j+1) not in seen: # right
                temp = seen.copy()
                traverse(i, j+1, k+1, temp)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                traverse(i, j, 0, set())
                
        return self.bool