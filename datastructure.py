def initialize():
	"""Purpose:
	"""
	mylist = []
	myqueue = []

	return [mylist, myqueue]

def add_to_structure(l,q,x):
	mylist.append(x)
	myqueue.append(x)

	print("mylist: ", mylist, ", myqueue: ", myqueue)

def remove_from_structure(l,q):
	mylist.pop()
	myqueue.pop(0)
	print("mylist: ", mylist, ", myqueue: ", myqueue)


if __name__ == "__main__":
	add_to_structure(initialize.get(0), initialize.get(1), 1)
