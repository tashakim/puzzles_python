import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    	"""Purpose: Finds kth largest element in array.
    	Note: Python's sorted() method uses Tim-sort, which 
    	has a time complexity same as merge sort. Hence O(n*log(n)).
    	"""
        return sorted(nums)[-k]
        

    def findKthLargest2(self, nums, k):
    	"""Purpose: Finds kth *largest* element in array.

    	Note: Python's heapq module supports min-heap.
    	Therefore, there is a way to efficiently max-heap 
    	and pop from root.
    	"""
    	heapq.heapify(nums)

    	for i in range(n-k):
    		heapq.heappop(nums)
    	return heapq.heapop(nums)