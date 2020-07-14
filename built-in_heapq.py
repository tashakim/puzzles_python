import heapq

"""Purpose: Create a min-heap and max-heap using the 
built-in heapq module in python3.
"""

myheap = []
mylist = [1,5,0,10,25,6,70,9,12]

# Pushing keys into heap:
for x in mylist:
	heapq.heappush(myheap, x) # Create min-heap

# Popping root of heap:
print("Popped root :", heapq.heappop(myheap)) # Pop min item in heap
print(myheap) # Resulting min-heap

print(heapq.nsmallest(5, myheap)) # Restricts heap size to k=5


print()
nums = [4,3,6,1,80,12,88,9]
heapq.heapify(nums)
print("My heap as min-heap:", nums)

nums2 = [4,3,6,1,80,12,88,9]
print("My heap with size 3 restriction: ",heapq.nlargest(3, nums))


"""How do we create a max-heap?
Answer: revert your keys, then call heapify().
"""
nums3 = [4,3,6,1,80,12,88,9]
heapq.heapify([-x for x in nums3])
print("My heap as max-heap: ", nums3)