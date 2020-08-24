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

	def countNodes_recursively(self, root):
		# Base case
		if not root:
			return 0
		# Recursive step: add num of nodes in left subtree, and right subtree.
		return self.countNodes_recursively(root.left) + self.countNodes_recursively(root.right) + 1


class Recurse:
	def getHeight(self, root):
		self.height = 0
		def postorder(root):
			if not root:
				return 0
			# Traverses binary tree via depth-frist traversal, starting at root.
			# Post-order is necessary, since we must decorate children before the node.
			left = postorder(root.left)
			right = postorder(root.right)
			# Decorate each node with a 'height' equal to one more than max of children.
			
			return updateHeight(root, left, right)

		def updateHeight(root, left, right):
			self.height = max(left, right) + 1 # Update height of tree to maximum of left and right subtree heights, plus one.
			return self.height 
		
		postorder(root)
		return self.height


	def getHeight_recursively(self, root):
		"""Purpose: Tree height is defined as max possible depth of nodes in a tree.
		"""
		# Base case
		if not root:
			return 0
		# Recursive step
		return max(self.getHeight_recursively(root.left), self.getHeight_recursively(root.right)) + 1


class MinMax:
	def computeMin(self, root):
		# Purpose: Traverses through the tree, and returns the minimum node value found.
		self.min = float('inf')
		def postorder(root):
			# Order is not important, as we will update global var 'min' while traversing whole tree.
			if not root:
				return None

			postorder(root.left)
			postorder(root.right)
			updateMin(root)


		def updateMin(node):
			# At each node, if node.val is less than global var 'min', update 'min'.
			if node.val < self.min:
				self.min = node.val
			return

		postorder(root)
		return self.min

	def computeMax(self, root):
		# Purpose: Traverses through the tree, and returns the maximum node value found.
		self.max = float('-inf')
		def postorder(root):
			if not root:
				return None

			postorder(root.left)
			postorder(root.right)
			updateMax(root)

		def updateMax(node):
			if node.val > self.max:
				self.max = node.val
			return

		postorder(root)
		return self.max


===========================================================================================================
# Adding tests here:
===========================================================================================================
def test_counting_nodes():
	t = Traverse()
	print("Result: ", t.countNodes(root))
	print("Result: ", t.countNodes_recursively(root))
	assert(t.countNodes(root) == t.countNodes_recursively(root)), "Something went wrong. Check your implementation!"

	print("\n[Success!] Counted nodes.\n")
	return

def test_height_computation():
	r = Recurse()
	print(r.getHeight_recursively(root))
	print(r.getHeight(root))
	assert(r.getHeight(root) == r.getHeight_recursively(root)), "Something went wrong. Check your implementation!"

	print("\n[Success!] Computed height.\n")
	return

def test_minmax_computation():
	m = MinMax()
	print("Min value of tree is: ", m.computeMin(root))
	print("Max value of tree is: ", m.computeMax(root))

	print("\n[Success!] Computed min and max values.\n")
	return



# Main script:
if __name__ == "__main__":
	root = Node(0)
	root.left = Node(1)
	root.right = Node(2)
	root.left.left = Node(3)
	root.left.right = Node(4)
	root.right.left = Node(5)


	tests = [test_counting_nodes, test_height_computation, test_minmax_computation]

	for test in tests:
		test()

	