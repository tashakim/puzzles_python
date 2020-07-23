class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    	"""Note: Each array will not contain repeating elements, 
    	because each array is strictly increasing.
    	"""
        if len(arr) == 2:
            return True
        arr.sort()
        standard = arr[1] - arr[0]
        for i in range(1, len(arr)-1):
            if arr[i+1] - arr[i] != standard:
                return False
        return True

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        mydict = {}

        for x in arr1:
            if x not in mydict:
                mydict[x] = 1
            else: mydict[x] += 1
        for x in arr2:
            if x not in mydict:
                mydict[x] = 1
            else: mydict[x] += 1
        for x in arr3:
            if x not in mydict:
                mydict[x] = 1
            else: mydict[x] += 1
        
        return [k for k,v in mydict.items() if v == 3]

    def arraysIntersection2(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    	"""Purpose: Uses more space!
    	"""
        mydict = {}
        myarr = arr1 + arr2 + arr3
        for x in myarr:
            if x not in mydict:
                mydict[x] = 1
            else: mydict[x] += 1
        
        return [k for k,v in mydict.items() if v == 3]

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        e = [x for x in A if x%2 == 0]
        o = [x for x in A if x%2 == 1]
        return e+o

class Solution:
    def sortArrayByParity2(self, A: List[int]) -> List[int]:
        return [x for x in A if x%2 == 0] + [x for x in A if x%2 == 1]