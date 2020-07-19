class Solution:
    def singleNumber0(self, nums: List[int]) -> int:
        """S.C: O(1), T.C: O(n log(n))
        """
        nums = sorted(nums) # O(n log(n))
        i = 0
        while i < len(nums)-1: # O(n)
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[-1] # -> Overall: O(n log(n))
    
    
    def singleNumber1(self, nums: List[int]) -> int:
        """S.C: O(n), T.C: O(n^2)
        """
        mystack = []
        for x in nums: # O(n)
            if x in mystack:
                mystack.remove(x) # O(n)
            else:
                mystack.append(x)
        return mystack.pop() # -> Overall: O(n^2)
    
    
    def singleNumber2(self, nums: List[int]) -> int:
        """S.C: O(n), T.C: O(n)
        """
        mydict = {}
        for x in nums: # O(n)
            if x in mydict:
                mydict[x] += 1
            else:
                mydict[x] = 1
        for i in mydict: # O(n)
            if mydict[i] == 1:
                return i # -> Overall: O(n)
        
    def singleNumber(self, nums: List[int]) -> int:
        """S.C: O(n), T.C: O(n)
        """
        return 2*sum(set(nums)) - (sum(nums))
        
        
        