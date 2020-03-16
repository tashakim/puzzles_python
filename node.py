class Node:
	def __init__(self, data):

		self._root = None
		self._right = None
		self._left = None
		self._value = data

	def printTree(self):
		print(self._value)

root = Node(10)
root.printTree()