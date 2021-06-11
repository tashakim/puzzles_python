# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def isSubtree(a, b):
	# Purpose: Checks if b is a subtree of b.
	def traverse(a):
		# Purpose: Traverses a to find a value equivalent to b.
		if not a:
			return False
		if a.val == b.val:
			if checkMatch(a, b):
				return True
		return traverse(a.left) or traverse(a.right)

	def checkMatch(a,b):
		# Purpose: Checks whether a and b are equivalent trees.
		if not a and not b:
			return True
		if (a and not b) or (not a and b):
			return False
		return a.val == b.val and checkMatch(a.left, b.left) and checkMatch(a.right, b.right)

	if not b: 
		return True

	return traverse(a)