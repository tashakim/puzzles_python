
class Node:
	def __init__(self, parent, data):
		self._root = None
		self._parent = parent
		self._left = None
		self._right = None
		self._value = data

	def printRoot(self):
		print(self._value)

	def root(self):
		return self._root

	def addLeft(self, parent, value):
		if value == None:
			raise InvalidInputException('value is null.')
		self._left = Node(parent, value)

	def left(self):
		return node._left

	def addRight(self, parent, value):
		if value == None:
			raise InvalidInputException('value is null')
		self._right = Node(parent, value)

	def right(self):
		return node._right



node = Node(None, 3)
node.printRoot()

left = node.addLeft(node.root(), 4)
node.left().printRoot()
