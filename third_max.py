class Solution:
    def __init__(self):
        self.max = float('-inf')
        self.second = float('-inf')
        self.third = float('-inf')
    
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        for item in nums:
            if item > self.max:
                if self.second != float('-inf') and self.max != float('-inf'):
                    self.third = self.second
                    self.second = self.max
                elif self.second == float('-inf') and self.max != float('-inf'):
                    self.second = self.max
                self.max = item
            else:
                if item > self.second:
                    if self.second == float('-inf'):
                        self.second = item
                    else:
                        self.third = self.second
                        self.second = item
                else:
                    if item > self.third:
                        self.third = item
                        
        if self.third != float('-inf'):
            return self.third
        else:
            return self.max