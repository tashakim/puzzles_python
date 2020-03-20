class Queue:

	def __init__(self):
		self._queue = [None]*5
		self._capacity = 5
		self._size = 0
		self._head = 0
		self._tail = 0

	def enqueue(self, object):
		if self._size == self._capacity:
			self._newqueue = [None]*(self._capacity*2)

			for i in range(0, self._capacity):
				self._newqueue[i] = self._queue[(self._head+i)%self._capacity]

			self._queue = self._newqueue

			self._head = 0
			self._queue[self._capacity] = object
			self._tail = self._capacity+1
			self._capacity =  self._capacity*2
			self._size +=1

		else:
			self._queue[self._tail] = object
			self._tail  +=1
			self._size +=1

		return

	def dequeue(self):
		return

	def size(self):
		return self._size

	def capacity(self):
		return self._capacity

	def head(self):
		return self._head

	def tail(self):
		return self._tail
	def queue(self):
		return self._queue

	def printDetails(self):
		print("\nCapacity: ", self.capacity(), "\n",
			"Size: ", self.size(), "\n", 
			"Head: ", self.head(), "\n",
			"Tail: ", self.tail(), "\n")
		

q = Queue()
q.printDetails()
print("Contents:")
print(q.queue()[:]) #convenient way of printing elements in an array


q.enqueue(1)
q.printDetails()
print("Contents: ")
print(q.queue()[:])

q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.printDetails()
print("Contents: ")
print(q.queue()[:])

q.enqueue(6)
q.printDetails()
print("Contents: ")
print(q.queue()[:])

q.enqueue(7)
q.printDetails()
print("Contents: ")
print(q.queue()[:])


