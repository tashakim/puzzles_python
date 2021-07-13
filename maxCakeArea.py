class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts):
        """
        Purpose: Returns max area of cake after we cut at each horizontal 
        and vertical position provided in input arrays. 

        Since answer can be large, return the answer modulo 10^9 + 7.
        """
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxWidth = width = horizontalCuts[0]
        horizontalCuts += [h]
        for i in range(len(horizontalCuts) - 1):
            width = horizontalCuts[i+1] - horizontalCuts[i]
            maxWidth = max(width, maxWidth)
            
        maxHeight = height = verticalCuts[0]
        verticalCuts += [w]
        for i in range(len(verticalCuts) - 1):
            height = verticalCuts[i+1] - verticalCuts[i]
            maxHeight = max(height, maxHeight)
            
        return (maxWidth * maxHeight) % (pow(10, 9) + 7)