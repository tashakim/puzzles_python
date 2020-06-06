def bfs(root):
	"""Purpose: Simple python implementation of breadth-first search
	"""
	q = [] # new queue
	q.append(root)
	while q not empty:
		node = q.pop(0)
		# visit node
		q.append(root.left())
		q.append(root.right())

if __name__ == "__main__":
	tree = BinTree()
	bfs(tree.root())