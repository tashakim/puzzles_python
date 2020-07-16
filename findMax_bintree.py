class Node:
	def __init__(self, value):
		self.value = value
		self.left = self.right = None

def findMax(root):
	if root == None:
		return float('-inf')

	leftmax = findMax(root.left) # recurse on left subtree
	rightmax = findMax(root.right) # recurse on right subtree

	m = max(leftmax, rightmax)
	return max(m, root.value) # return max. from root, left subtree, and right subtree.

if __name__ == "__main__":
	root = Node(2)
	root.left = Node(7)
	root.right = Node(5)
	root.left.right = Node(6)
	root.left.right.left = Node(1)
	root.left.right.right = Node(11)
	root.right.right = Node(9)
	root.right.right.left = Node(4)

	print(findMax(root))