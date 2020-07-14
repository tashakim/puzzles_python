import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            stones = [-x for x in stones]
            heapq.heapify(stones)
            largest =  -1*heapq.heappop(stones) 
            runnerup = -1*heapq.heappop(stones)
            stones = [-x for x in stones]
            if largest != runnerup:
                num = largest - runnerup
                heapq.heappush(stones, num)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    assert(s.lastStoneWeight([2,7,4,1,8,1]) == 1), "Wrong answer"

    print("Test passed!")