class Tree:
	def __init__(self, root):
		self._root = root
		print("new  giving tree created")

	def root(self):
		return self._root

	def addChild(self, child):
		self._child = child

	def child(self):
		return self._child

	def give(self):
		self._seedling = Tree(99)
		return self._seedling 

class Receiver:
	def __init__(self, name):
		self._name = name
		print("A receiver named ", name, "wants to receive.")


if __name__ == "__main__":
	mytree = Tree(3)
	print("Your root is: ", mytree.root())

	mytree.addChild(1)
	print("Your child is: ", mytree.child())

	print("Tree wants to give..")

	gift = mytree.give()
	print(gift.root())


	newReceiver = Receiver("Tasha")

