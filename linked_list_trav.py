class Node:
	def __init__ (self, value):
		self.val = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, node):
		node = Node(node.val)
		if self.head == self.tail == None:
			self.head = node
		else:
			self.tail = node
			self.tail.next = None
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
	print(l1)