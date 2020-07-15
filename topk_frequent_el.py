import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """Purpose: Given a non-empty array of integers, returns the k most frequent elements.
    """
        mydict = {}
        for x in nums:
            if x in mydict.keys():
                mydict[x] += 1
            else:
                mydict[x] = 1
        l = []
        myheap = [(value, key) for key,value in mydict.items()]
        for i in heapq.nlargest(k, myheap):
            l.append(i[1])
        return l