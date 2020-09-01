# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Traversals:
	def preorder_recursive(self, root):
		def helper(root, res):
			if not root:
				return None
			# add root to res
			res.append(root.val)
			helper(root.left, res)
			helper(root.right, res)

		res = []
		helper(root, res)
		return res



	def preorder_iterative(self, root):
		visited, order = [root], []
		while visited:
			popped = visited.pop()
			# decorate root
			if popped:
				order.append(popped.val)
			if popped.right:
				visited.append(popped.right)
			if popped.left:
				visited.append(popped.left)
		return order



	def breadth_first(self, root):
		visited, order = [root], []
		while visited:
			popped = visited.pop(0)
			order.append(popped.val)
			if popped.left:
				visited.append(popped.left)
			if popped.right:
				visited.append(popped.right)
		return order