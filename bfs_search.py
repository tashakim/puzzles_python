def bfs(root):
	"""Purpose: Simple python implementation of breadth-first search
	"""
	q = [] # new queue
	q.append(root)
	while q not empty:
		visited = q.pop(0) # visit node
		
		q.append(root.left()) # either order works!
		q.append(root.right())

def dfs(root):
	"""Purpose: Depth-first search implementation.
	"""
	s = [] # new stack
	s.append(root)
	while s not empty:
		visited = s.pop(0) # visit node
		s.append(root.left())
		s.append(root.right())


if __name__ == "__main__":
	tree = BinTree()
	bfs(tree.root())