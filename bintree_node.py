class Node:
	"""Purpose: Implements a node of a binary tree.
	"""
	def __init__(self, parent, value):
		"""Purpose: Constructor for a node
		Example: Node(None, 3) -> Root node with value 3.
		"""
		self._parent = parent
		self._value = value
		self._left = None
		self._right = None

	def __str__(self):
		"""Purpose: String representation of the node.
		"""
		result = ""
		result += "value: "
		result += repr(self.value())

		result += "; Left: "
		if(self.hasLeft()):
			result += str(self.left())
		else:
			result += "Nothing"

		result += "; Right: "
		if self.hasRight():
			result += str(self.right())
		else:
			result += "Nothing"
		result += ")"

		return result 


	def parent(self, node):
		return self._parent

	def left(self):
		return self._left

	def right(self):
		return self._right

	def children(self):
		"""Purpose: returns the children of node.
		"""
		return [self._left, self._right]

	def addLeft(self, value):
		"""Purpose: adds left child to this node.
		"""
		if(self.hasLeft()):
			print("Node already has a left child.")
			return self._left

		return self._left = Node(self, value)

	def addRight(self, value):
		"""Purpose: adds right child to this node.
		"""
		if(self.hasRight()):
			print("Node already has a right child.")
			return self.right

		return self._right = Node(self, value)

	def hasLeft(self):
		"""Purpose: returns a boolean, indicating whether this node has a left node or not.
		"""
		return self._left != None

	def hasRight(self):
		"""Purpose: returns a boolean, indicating whether this node has a right node or not.
		return self._right != None


	def value(self):
		return self._value

	def depth(self):
		"""Purpose: Returns the depth of this node.
		"""
		return 



