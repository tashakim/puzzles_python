class Node(self, v):
	self.data = v
	self.next = None

class LinkedList(self):
	self.head = None
	self.tail = None

	def search(self, key):
		node = self.head
		while node and node != key:
			node = node.next
		return node

	def insert_after(self, node, new):
		new.next = node.next
		node.next = new


	def delete_after(self, node):
		node.next = node.next.next

