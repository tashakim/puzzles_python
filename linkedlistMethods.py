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

	def insertAt(self, p, node):
		if(p < 1 or p > self._count):
			raise InvalidIndexException("Index is invalid.")
		self.getTo(p-1)._next = node
		node.next = self.getTo(p)

	def popAt(self, pos):
        if(pos < 1 or pos > self.nodeCount):
            raise IndexError
        target = self.getAt(pos)
        if(self.nodeCount == 1): # single node Linked-list
            self.head = None
            self.tail = None
        elif(pos == 1): # pop head node
            self.head = self.getAt(pos +1)
        else:
            prev = self.getAt(pos -1)
            
            if(pos == self.nodeCount): # pop tail node
                prev.next = None
                self.tail = prev
            else: # pop middle node
                prev.next = self.getAt(pos+1)
        self.nodeCount -=1
        return target.data
    

	def concat(self, L):

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
