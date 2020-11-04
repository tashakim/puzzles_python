class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        ht = dict()
        for x in pieces:
            ht[x[0]] = x
        ptr = 0
        while ptr < len(arr):
            if arr[ptr] in ht:
                n = len(ht[arr[ptr]])
                if arr[ptr: ptr+n] != ht[arr[ptr]]:
                    return False
                ptr += n
            else:
                return False
        return True

    def canFormArray1(self, arr: List[int], pieces: List[List[int]]) -> bool:
        res = []
        ht = {x[0]:x for x in pieces}
        i = 0
        while i < len(arr):
            res += ht[arr[i]]
            i += len(ht[arr[i]])
        return res == arr

    def canFormArray2(self, arr: List[int], pieces: List[List[int]]) -> bool:
        res = []
        ht = {x[0]:x for x in pieces}
        for item in arr:
            res += ht.get( item, [] )
        return res == arr