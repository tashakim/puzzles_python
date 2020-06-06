class DFS_traversals():
	"""Purpose: Python implentation of three (3) different 
	types of depth-first search (Dfs) traversal orders:
	preorder, postorder, and inorder.
	"""
	def __init__(root, order):
		s = [] # new stack
		s.append(root)
		visited = []
		while s not empty:
			visit(root, order, s, visited)

	def visit(order, node, s, visited):
		if(order == "preorder"):
			preorder(node, s, visited)

		if(order == "postorder"):
			postorder(node, s, visited)

		if(order == "inorder"):
			inorder(node, s, visited)

	def preorder(node, s, visited):
		visited = s.pop(0)
		if(node hasLeft()):
			preorder(node.left(), s)
		if(node hasRight()):	
			preorder(node.right(), s)

	def postorder(node, s, visited):
		if(node hasLeft()):
			postorder(node.left(), s)
		if(node hasRight()):
			postorder(node.right(), s)
		visited.append(node)

	def inorder(node, s, visited):
		if(node hasLeft()):
			inorder(node.left(), s)
		visited.append(node)
		if(node hasRight()):
			inorder(node.right(), s)


if __name__ == "__main__":	
	dfs = DFS_traversals()
	dfs.preorder(root)