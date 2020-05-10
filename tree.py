class Tree:
	def __init__(self, root):
		self._root = root
		print("new  giving tree created")

	def root(self):
		return self._root



if __name__ == "__main__":
	mytree = Tree(3)
	print("Your root is: ", mytree.root())