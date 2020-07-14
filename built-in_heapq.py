import heapq

myheap = []
mylist = [1,5,0,10,25,6,70,9,12]
for x in mylist:
	heapq.heappush(myheap, x) # Create min-heap
print(heapq.heappop(myheap)) # Pop min item in heap
print(myheap) # resulting min-heap