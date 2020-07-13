class Solution:
    def __init__(self):
        self.max = float('-inf')
        self.second = float('-inf')
        self.third = float('-inf')
    
    def thirdMax(self, nums):
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

if __name__ == "__main__":
    s = Solution()
    assert(s.thirdMax([3,2,1]) == 1), "Wrong answer" # Checks duplicates    
    s = Solution()
    assert(s.thirdMax([3,3,3]) == 3), "Wrong answer" # Checks duplicates
    s = Solution()
    assert(s.thirdMax([1,2]) == 2), "Wrong answer" # Returns max, since third max DNE
    s = Solution()
    assert(s.thirdMax([1,2,3,4,5]) == 3), "Wong answer"
    s = Solution()
    assert(s.thirdMax([0]) == 0), "Wrong answer"

    print("All tests passed!")