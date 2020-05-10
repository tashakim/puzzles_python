class Tree:
	def __init__(self, root):
		self._root = root

	def root(self):
		return self._root


if __name__ == "__main__":
	mytree = Tree(3)
	print(mytree.root())