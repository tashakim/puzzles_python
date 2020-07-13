class Solution:
    def __init__(self):
        self.stack = []
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for item in nums:
            self.downstack(item)
        print(self.stack)
        return self.stack[-k]
            
    def downstack(self, item):
        if self.stack == []:
            self.stack.append(item)
        if item >= self.stack[-1]:
            self.stack.append(item)
        else:
            popped = self.stack.pop()
            downStack(self.stack,item)
            self.stack.append(popped)
        return self.stack