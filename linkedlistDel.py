class LinkedList:
	def __init__(self):
		self._head = None

	def __repr__(self):
		node = self._head
		nodes = []
		while node is not None:
			nodes.append(node._value)
			node = node._next
		nodes.append("None")
		return "->".join(nodes)


class Node:
	def __init__(self, value):
		self._value = value
		self._next = None

	def __repr__(self):
		return self._value


def linkedlistDel1(n):
	"""Purpose: Takes in a node n, and deletes
	the node after node n. 
	Runtime complexity: O(1)
	"""
	return


def linkedlistDel2(n, head):
	"""Purpose: Takes in a node n, and a node 
	head, and removes n from the list, where
	head is the first node in the list.
	Runtime complexity: O(k)
	"""
	return


def smartDel(n):
	"""Purpose: Removes a node n from the list.
	Runtime complexity: O(1)
	"""
	return

def test():
	pass


if __name__ == "__main__":
	L = LinkedList()
	firstnode = Node("A")
	L._head = firstnode
	print(L)
	test()