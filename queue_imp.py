class EmptyQueueException():
	pass

class MyQueue:
	"""Purpose: Simple python implementation of Queue ADT.
	"""
	def __init__(self):
		self._data = []
		return

	def push(self, item):
		self._data.append(item)
		return


	def pop(self):
		if(self._data == None):
			raise EmptyQueueException("Queue is empty.")
		popped = self._data.pop(0)
		return popped

	def printQueue(self):
		if(self._data == []):
			print("Queue is empty.")
		print(self._data)
		return


if __name__ == "__main__":
	q = MyQueue()
	for i in range(5):
		q.push(i)

	q.printQueue()
	for i in range(2):
		q.pop()
	q.printQueue()