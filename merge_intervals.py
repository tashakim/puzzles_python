class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    """Purpose: Given a collection of integer intervals, 
    merges all overlapping intervals.
    """
        intervals.sort() # O(1) ~ O(n) S.C.
        
        merged = []
        for x in intervals:
            if not merged or merged[-1][1] < x[0]:
                merged.append(x)
            else:
                merged[-1][1] = max(merged[-1][1], x[1])
                
        return merged