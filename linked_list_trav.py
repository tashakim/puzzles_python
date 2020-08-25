class Node:
	def __init__ (self, value):
		self.val = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, node):
		if self.head == self.tail == None:
			self.tail = node
			self.tail.next = None
			self.head = self.tail
			self.tail = self.tail.next

		else:
			self.tail = node
			self.tail.next = None
			self.tail = self.tail.next
		return
		

	def printValues(self):
		if not self.head:
			return None

		cur = self.head
		while cur:
			print(cur.val)
			cur = cur.next
		return 
	"""
	def delete(self, node):

	def 
	"""
if __name__ == "__main__":
	n = Node(0)
	print(n.val)
	print(n.next)

	l1 = LinkedList()

	l1.insert(n)
	l1.printValues()
	print(l1.head.val)
	
	n2 = Node(1)
	l1.insert(n2)
	print(l1.head.val)
	l1.printValues()
	