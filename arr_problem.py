class Solution:
"""Purpose: Returns boolean indicating if each kid can have the 
greatest number of candies if given extraCandies.
"""
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [k + extraCandies >= m for k in candies]

class Solution:
"""Purpose: Returns the number of pairs (i,j) s.t. nums[i] == nums[j] and i<j, given an array of integers 'nums'.
"""
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l = []
        for x in list(set(nums)):
            l.append(nums.count(x))
        sum = 0
        for x in l:
            sum += x*(x-1)//2
        return sum

    def numIdenticalPairs2(self, nums: List[int]) -> int:
    """Note: Runtime 32 ms, faster than 93.01% submissions;
    S.C: 13.8MB, less than 100% of submissions.
    """
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count +=1
        return count

class Solution:
	"""Purpose: Given string 'S', removes vowels 'a', 'e', 'i', 'o', 'u' from it, returning a new string.
	"""
    def removeVowels0(self, S):
        for i in S:
            if i in ['a', 'e', 'i', 'o', 'u']:
                S = S.replace(i, "")
        return S

    def removeVowels1(self, S):
        return "".join(c for c in S if c not in "aeiou")
    
    def removeVowels2(self, S):
        S = S.replace('a', "")
        S = S.replace('e', "")
        S = S.replace('i', "")
        S = S.replace('o', "")
        S = S.replace('u', "")
        return S
    

class Solution:
	"""Purpose: Given an array of integers with 2n elements, 
	shuffles the elements so that [x1, x2, ..., y1, y2] -> [x1, y1, ... , xn, yn].
	"""
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x,y = nums[:n], nums[n:]
        arr = []
        for i in range(n):
            arr.append(x.pop(0))
            arr.append(y.pop(0))
        return arr