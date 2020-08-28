class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
    """Purpose: Returns the number of students working at time queryTime. 

    Time complexity: O(n)
    Space complexity: O(n) worst case.
    """
        # for given input queryTime, 
        potential, res = [], []
        # loop through startTime, to see if any x <= querTime, where x in startTime
        for i, x in enumerate(startTime):
            if x <= queryTime:
                potential.append(i)
        
        for i, x in enumerate(endTime):
            if x >= queryTime and i in potential:
                res.append(i)
                
        return len(res)