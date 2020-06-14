#!usr/bin/python3

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
	# Here we assume that a pointer to node n is already known.

	n._next = None # deletes 'next' node.
	n._next = n._next._next # resets pointer to node after next.
	return


def linkedlistDel2(n, head):
	"""Purpose: Takes in a node n, and a node 
	head, and removes n from the list, where
	head is the first node in the list.
	Runtime complexity: O(k)
	"""
	# Here we traverse through linked list and remove node n from it.
	s = head
	for i in range(len(L)): 
		if(s == n):
			s._value = None
		s = s._next

	return


def smartDel(n):
	"""Purpose: Removes a node n from the list.
	Runtime complexity: O(1)
	"""
	# We use ._value and ._next fields.
	# n._value = None (resets value of node n. We don't even need this.)
	n._next = n._next._next
	return


def test():
	l = LinkedList()
	firstnode = Node("1")
	l._head = firstnode

	secondnode = Node("2")
	firstnode._next = secondnode
	thirdnode = Node("3")
	secondnode._next = thirdnode

	print(l)
	pass


if __name__ == "__main__":

	L = LinkedList()
	firstnode = Node("A")
	L._head = firstnode
	print(L)

	test()