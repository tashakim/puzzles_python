class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """Purpose: Inserts a new interval into a set of 
    non-overlapping intervals, merging intervals when 
    necessary.
    """
        intervals.append(newInterval)
        intervals.sort()
        
        merged = []
        for x in intervals:
            if not merged or merged[-1][1] < x[0]:
                merged.append(x)
            else:
                merged[-1][1] = max(merged[-1][1], x[1])
        return merged