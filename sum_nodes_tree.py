class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Traverse:
	def countNodes(self, root):
		self.count = 0

		def preorder(root):
			# Traverses binary tree via depth-first traversal, starting at root.
			print("call preorder")
			decorate(root) # decorate node here 

			if root.left:
				preorder(root.left)
			if root.right:
				preorder(root.right)

		def decorate(root):
			# Purpose: count increases for each node.
			print(root.val, " has been visited.")
			self.count += 1
			return 

		preorder(root)
		return self.count


if __name__ == "__main__":
	root = Node(0)
	root.left = Node(1)
	root.right = Node(2)
	root.left.left = Node(3)
	root.left.right = Node(4)
	root.right.left = Node(5)

	t = Traverse()
	
	print("Result: ", t.countNodes(root))
	
