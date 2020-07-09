class MinStack:

    def __init__(self):
        """
        Initializes the data structure here.
        """
        self.stack = []
        self.currMin = float('inf')
        self.size = 0

    def push(self, x: int) -> None:
        if(x < self.currMin):
            self.currMin = x
        self.stack.append([x, self.currMin])
        self.size += 1

    def pop(self) -> None:
        if(self.size > 0):
            self.stack.pop(-1)
            self.size -=1
        # reset currMin when stack is Empty.
        if(self.size == 0):
            self.currMin = float('inf')
        else:
            # reset currMin when item is popped from stack. 
            self.currMin = self.stack[-1][1]
        

    def top(self) -> int:
        if(self.size >0):
            return self.stack[-1][0]
        else:
            return -1

    def getMin(self) -> int:
        if(self.size > 0):
            return self.stack[-1][1]
        else:
            return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()