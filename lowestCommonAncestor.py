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