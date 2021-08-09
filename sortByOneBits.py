class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        Purpose: Sort the integers in `arr` in ascending order, by 
        the number of 1's in their binary representation. 

        Note: For integers with same number of 1's, sort them in ascending order.
        
        """
        def customSort(x):
            # Defines custom sorting order
            b = bin(x)[2:]

            return b.count('1'), x # first sort by no. of 1's, next by number.
        
        return sorted(arr, key=lambda x: customSort(x))