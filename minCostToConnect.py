import heapq

class Solution:
    """
    Purpose: Given sticks with positive int lengths, connect all sticks
    two at a time until there is only one stick remaining, and return the 
    minimum cost connecting all given sticks into one stick.
    """
    def connectSticks(self, sticks: List[int]):
        """
        Purpose: sorts sticks every iteration, and continues to connect 
        the two shortest sticks, adding cost to resulting cost.

        Note: Inefficient solution, python's timsort has a time complexity
        recorded at O(n * log(n)). Iterating through every next element and 
        sorting would therefore result in O(n * n * log(n)). 

        """
        def sort_sticks(sticks, res):
            sticks.sort()

            cur_sum = sticks[0] + sticks[1]
            res += cur_sum
            
            sticks.pop(0)
            sticks.pop(0)
            sticks.append(cur_sum)

            return sticks, res
        
        res = 0
        while len(sticks) > 1:
            sticks, res = sort_sticks(sticks, res)
            
        return  res


    def connectSticks2(self, sticks: List[int]):
        """
        Purpose: We can improve the above solution using a min-heap.
        We will use python's built in module heapq.
        """
        res = 0
        heapq.heapify(sticks)
        
        while len(sticks) > 1:
            cur_cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            
            heapq.heappush(sticks, cur_cost)
            res += cur_cost
            
        return res