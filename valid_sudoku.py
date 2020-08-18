import collections

class Solution(object):
	"""Purpose: Returns if sudoku board is valid.
	Uses helper method to check for each 3x3 neighbor.
	"""
    def isValidSudoku(self, grid):

        def checkNeighbors(box, i, j):
            myset = set()
            for hcell in range(i, i + len(box)//3):
                for vcell in range(j, j+len(box)//3):
                    if box[hcell][vcell] != '.':
                        if box[hcell][vcell] not in myset:
                            myset.add(box[hcell][vcell])
                            print(myset)
                        else:
                            return False
            return True
        
        # make collections Count of each row
        for row in grid:
            for k,v in collections.Counter(row).items():
                if v > 1 and k != '.':
                    return False

        # make collections Count of each col
        for col in range(len(grid[0])):
            for k, v in collections.Counter([row[col] for row in grid]).items():
                if v > 1 and k != '.':
                    return False

        # for each 3x3 grid-box (start at (2,2) -> (2+3k, 2+3k),...)
        for i in range(len(grid)//3):
            for j in range(len(grid)//3):
                if not checkNeighbors(grid, 3*i, 3*j):
                    return False

        return True



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

