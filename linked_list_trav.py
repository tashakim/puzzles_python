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

	def delete(self, node):

	def 