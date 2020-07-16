class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def sizeOfTree(node):
		if node:
			return sizeOfTree(node.left) + sizeOfTree(node.right) + 1
		else:
			return 0

if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.right.right = Node(5)

	sizeOfTree(root)