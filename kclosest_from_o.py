import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """Purpose: Uses heap to return K closest points 
        from the origin, time complexity: O(n log(n)).
        """
        dist = {}

        for i in range(len(points)):
            dist[i] = int(points[i][0]**2 + points[i][1]**2)
        mylist = [(val, key) for key,val in dist.items()]
        
        i = []
        heapq.heapify(mylist)
        for k in range(K):
            i.append(heapq.heappop(mylist)[1])
        
        return [points[x] for x in i]
        