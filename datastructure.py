def initialize():
	"""Purpose:
	"""
	mylist = []
	myqueue = []

	return [mylist, myqueue]

def add_to_structure(l,q,x):
	mylist.append(x)
	myqueue.append(x)

	print("mylist: ", l, ", myqueue: ", q)

def remove_from_structure(l,q):
	mylist.pop()
	myqueue.pop(0)
	print("mylist: ", l, ", myqueue: ", q)


if __name__ == "__main__":
	add_to_structure(initialize()[0], initialize()[1], 1)
