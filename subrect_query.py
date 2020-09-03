class SubrectangleQueries:
    
    def __init__(self, rectangle: List[List[int]]):
        self.data = {}
        for j in range(len(rectangle[0])):
            for i in range(len(rectangle)):
                self.data[(i,j)] = rectangle[i][j]            

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.data[(i,j)] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.data[(row, col)]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1, col1, row2, col2, newValue)
# param_2 = obj.getValue(row, col)