class Solution:
    def countBattleShips(self, board: List[List[str]]) -> int:
        """
        Purpose: Given a m x n matrix board, where each cell indicates part of a battleship
        'X', or empty '.', 
        returns the number of battleships on board.

        Note: Each battleship can only be placed horizontally or vertically on the board.

        """
        count = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if (i==0 or board[i-1][j]=='.') and (j==0 or board[i][j-1]=='.'):
                        count += 1
                        
        return count
                        