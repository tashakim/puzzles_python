import heapq

# Finds 4th largest item in heap:
nums = [4,3,6,1,80,12,88,9]
print(heapq.nlargest(4, nums)[-1])


# A little more convoluted method for creating max-heap:
nums = [4,3,6,1,80,12,88,9]
nums = [-x for x in nums]
heapq.heapify(nums)
for i in range(3):
	heapq.heappop(nums)
print(-1*heapq.heappop(nums))