class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # Purpose: Returns true if the summation of the numerical values of 
        # firstWord, secondWord equals the numerical value of targetWord, False otherwise.

        print(ord('a') - 97) # a = 0, b = 1, ...
        res1, res2, res3 = [], [], []
        for c in firstWord: 
            res1.append(str(ord(c) - 97))
        a = ''.join(res1) # ''.join([str(ord(c) - 97) for c in firstWord])
                    
        for c in secondWord:
            res2.append(str(ord(c) - 97))
        b = ''.join(res2) 
    
        for c in targetWord:
            res3.append(str(ord(c) - 97))
        c =''.join(res3)
        
        if int(a) + int(b) == int(c):
            return True
        return False


    def isSumEqual2(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # Purpose: Same as above, uses list comprehension.
        return int(''.join([str(ord(c) - 97) for c in firstWord])) + \
        int(''.join([str(ord(c) - 97) for c in secondWord])) == \
        int(''.join([str(ord(c) - 97) for c in targetWord]))


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # Purpose: Checks if at most one edit can make a non-decreasing array.
        bool = False
        def check(arr, bool):
            i = 0
            while i < len(arr)-1:
                if arr[i+1] < arr[i]:
                    if bool == False:
                        bool = True
                        temp = arr.copy()
                        temp.pop(i)
                        arr.pop(i+1)
                        return check(temp, bool) or check(arr, bool)
                    else:
                        return False
                i += 1 
            return True
        return check(nums, bool)