import heapq
class Solution:
    def findContentChildren(self, g, s):
        """
        Purpose: Given greed factor g[i] of each child, returns the max. number
        of children that are content after distributing cookies of size s[i].

        Note: A child is content if they eat a cookie that has size greater than 
        or equal to their greed factor.

        Sample Input: g = [1,2,3], s= [1,1]
        Sample Output: 1
        """
        g.sort()
        s.sort()
        
        child = cookie = 0
        num_cookies = len(s)
        num_children = len(g)
        
        while cookie < num_cookies and child < num_children:
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        
        return child


    def findContentChildren1(self, g, s):
        """
        Purpose: Min. heap approach.
        """
        heapq.heapify(s)
        count = 0
        g.sort()
        for child in g:
            # end if no cookies exist
            if not s: return count
            x = float('-inf')
            while x < child and s:
                x = heapq.heappop(s)

            if x >= child:
                count += 1

        return count
