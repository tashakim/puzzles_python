class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """Purpose: Returns whether a list of three points in the plane
        are a boomerang.

        Note: A boomerang consists of three points that don't lie in a 
        straight line. The points must also be distinct.
        """
        for x in points:
            if points.count(x) > 1:
                return False
        
        # account for zero-division error
        if (points[2][1]-points[1][1]) == 0 or (points[1][1]-points[0][1])==0:
            if (points[2][0]- points[1][0])*(points[1][1]-points[0][1]) == (points[1][0]-points[0][0])*(points[2][1]-points[1][1]):
                return False

        # verify slope
        elif (points[2][0]- points[1][0])/(points[2][1]-points[1][1]) == (points[1][0]-points[0][0])/(points[1][1]-points[0][1]):
            return False

        return True