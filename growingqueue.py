class MyQueue():
	def __init__(self, cap):
		self._capacity = cap
		self._queue = [None]*cap
		self._size = 0
		self._head = self._tail = 0

	def size(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def enqueue(self, item):
		self._queue[self._head] = item
		print("\nAdded ", item, " to queue.\n")


		if(self._head +1 >= self._capacity and self._size == self._capacity):
			self._capacity = self._capacity*2
			self._queue = [None]*self._capacity
		self._head +=1
		self._size +=1
		return

	def dequeue(self):
		popped = self._queue[self._tail] 
		self._tail += 1
		return popped

	def front(self):
		return self._head

	def capacity(self):
		return self._capacity

if __name__ == "__main__":
	q = MyQueue(3)
	print("Is queue empty? : ",q.is_empty())
	print("Capacity of queue is : ", q.capacity())
	q.enqueue(1)
	print("size of queue is : ", q.size())
	q.enqueue(1)
	q.enqueue(1)
	q.enqueue(1)
	print("size of new queue is : ", q.size())
	print(q._head)
	print("capacity of new queue is : ", q.capacity())
