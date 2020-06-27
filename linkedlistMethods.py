class InvalidIndexException(Exception):
	pass

class Node:
	def __init__(self, item):
		self._data = item
		self._next = None

class LinkedList:
	def __init__(self):
		self._head = None
		self._tail = None
		self._count = 0

	def getTo(self, p):
		if(p < 1 or p > self._count):
			raise InvalidIndexException("Index is invalid.")
		curr = self._head
		count = 1
		while(count < p):
			curr = curr._next
			count += 1
		return curr

	def traverse(self):
		curr = self._head
		items = []
		while(curr != None):
			items.append(curr._data)
			curr = curr._next
		return items

if __name__ == "__main__":
	mylist = LinkedList()
