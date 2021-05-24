class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr) -1
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                index = i
                arr[-1] = 0
                while index < n-1:
                    arr[index+1], arr[-1] = arr[-1], arr[index+1]
                    index += 1
                i += 1
            i += 1
        return 
            