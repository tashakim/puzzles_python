def find(node, x):
	"""Purpose:
	"""
	if(node.value() == x):
		return node
	elif(x < node.value() and node.left() != None):
		return find(node.left(), x)

	elif(x > node.value() and node.right() != None):
		return find(node.right(), x)

	return None

def insert(node, x):
	if(node.value() == x):
		return

	if(x  < node.value()):
		if(node.left() == None):
			node.addLeft(x)
		else:
			insert(node.left(), x)
	else:
		if(node.right() == None):
			node.addRight(x)
		else:
			insert(node.right(), x)

def remove(node, x):
	if(!node.hasChildren()):
		node.parent().removeChild(node)

	elif(node.hasLeft() and !node.hasRight()):
		if(node.parent().left() == node):
			node.parent().left() = node.left()
		else:
			node.parent().right() = node.left()

	elif(node.hasRight() and !node.hasLeft()):
		if(node.parent().left() == node):
			node.parent().left() = node.right()
		else:
			node.parent().right() = node.right()
		else:
			node.next() = successor(node)
			node.value() = node.next().value()
			remove(node.next())


if __name__ == "__main__":
	tree = BST()
	find(tree.root(), 3)