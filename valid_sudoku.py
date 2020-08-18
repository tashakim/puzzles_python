class Solution(object):
    def isValidSudoku(self, board):
    """Purpose: Returns whether or not a Sudoku board is valid.
 	Note: clean solution
    """
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i//3,j//3,c)]
        return len(seen) == len(set(seen))
