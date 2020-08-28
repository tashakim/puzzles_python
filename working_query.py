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

    def busyStudent(self, startTime, endTime, queryTime):
        """Purpose: Reduces space complexity of above solution, by keeping track of
        only the number of potential students - and looping through two arrays 
        simultaneously.

        """
        potential, num = [], 0
        for i, x in enumerate(startTime):
            if x <= queryTime and endTime[i] >= queryTime:
                num += 1
        return num