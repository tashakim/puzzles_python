class Solution:
    def __init__(self):
        self.stack = []
        
    def findKthLargest(self, nums: List[int], k: int) -> int: # exceeds time limit
        for item in nums:
            self.downstack(item)
        return self.stack[-k]
            
    def downstack(self, item):
        if self.stack == []:
            self.stack.append(item)
            return self.stack
        if item >= self.stack[-1]:
            self.stack.append(item)
        else:
            popped = self.stack.pop()
            self.downstack(item)
            self.stack.append(popped)
        return self.stack

if __name__ == "__main__":
    s = Solution()
    assert(s.findKthLargest([3,2,1,5,6,4], 2) == 2), "Wrong answer"
    assert(s.findKthLargest([1,2], 2 ) == 1), "Wrong answer"
    assert(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4), "Wrong answer"
    
    print("All tests passed!")