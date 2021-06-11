
# Can we find the lowest common ancestor of two nodes given the root of a binary tree?

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def lowestCommonAncestor(self, root, p, q):
	# Purpose: Recursively finds the lowest common ancestor nodes given two nodes.
	if not root: return None
	if root == p or root == q:
		return root

	left = self.lowestCommonAncestor(root.left, p, q)
	right = self.lowestCommonAncestor(root.right, p, q)

	if left and right: 
		return root

	if not left: return right
	if not right: return left


# What if we don't have information about the root of the tree?
def lowestCommonAncestor2(self, p, q):
	# Purpose: Finds the root of tree first, then same logic as above.
	# S: O(1)
	root = p
	while root.parent:
		root = root.parent

	def LCA(root, p, q):
		if not root: return None
		if root == p or root == q:
			return root

		left = LCA(root.left, p, q)
		right = LCA(root.right, p, q)

		if left and right: 
			return root
		if not left: return right
		if not right: return left

	return LCA(root, p, q)

# Cool solutions:
def lowestCommonAncestor3(self, p, q):
	# Purpose: Solution using two pointers. Turning into finding intersection of a linked list questin.
	# S: O(1)
	ptr1 = p
	ptr2 = q
	while ptr1 != ptr2:
		if ptr1.parent: 
			ptr1 = ptr1.parent
		else: ptr1 = q

		if ptr2.parent:
			ptr2 = ptr2.parent
		else: ptr2 = p

	return ptr1


